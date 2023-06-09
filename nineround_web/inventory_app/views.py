from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Inventory, EventItems # import models
from django.db.models import Q, F
from .forms import EventForm


# Create your views here.
def events(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    events = Event.objects.all()
    events = Event.objects.filter(
        Q(nama__icontains=q) |
        Q(lokasi__icontains=q) |
        Q(status__icontains=q)
    )
    context = {'events': events}

    return render(request, 'inventory_app/event.html', context=context)
    # return HttpResponse('Home Page')


def newEvent(request):
    form = EventForm()
    # buat list barcode apabila belum ada
    if 'barcode' not in request.session:
        request.session['barcode'] = []
    # apabila klik submit-button atau delete-item, maka
    if request.method == 'POST':
        form = EventForm(request.POST)
        
        if form.is_valid() and request.POST.get("additem-button"):
            if request.POST['barcode-input'] in Inventory.objects.values_list('id', flat=True) and request.POST['barcode-input'] not in request.session['barcode']:
                request.session['barcode'] += [request.POST['barcode-input']]
        elif form.is_valid() and request.POST.get("submit-button"):
            new_event = Event(nama=request.POST['nama'],
                              lokasi= request.POST['lokasi'],
                              tanggal_mulai = request.POST['tanggal_mulai'],
                              tanggal_berakhir = request.POST['tanggal_berakhir']
                              )
            new_event.save()
            for item in request.session['barcode']:
                new_event_item = EventItems(events_id = Event.objects.latest('id').id,
                                            items_id = item,
                                            status_in_event = 'Barang tersedia'
                                            )
                new_event_item.save()
            request.session.flush()
            return redirect('events')
            # !!!!! add return to home to remove error
        elif request.POST.get('cancel-button'):
            if request.session['barcode']:
                request.session.flush()
            return redirect('events')
        elif form.is_valid() and request.POST.get("delete-button"):
            deleted_id = request.POST.getlist('items_to_delete')
            for i in deleted_id:
                request.session['barcode'].remove(i)
    request.session.modified = True
    items = Inventory.objects.filter(id__in=request.session['barcode']).order_by('id')
    context = {'form':form, 'items':items}
    return render(request, 'inventory_app/new-event.html', context=context)


def eventDetail(request, pk):
    event_details = Inventory.objects.filter(eventitems__events=pk) # query all items in Inventory, dimana events id sama dengan pk yang dipassing (many to many relationship). Python memberikan kemudahan bagi developer untuk melakukan lookup dengan menggunakan *namaTabelLain*__*kolomTabelLainTersebut*
    events = Event.objects.filter(id=pk)
    context = {'event_details':event_details, 'events':events}

    return render(request, 'inventory_app/event-detail.html', context=context)


def addItemsToEvent(request, pk):
    # additional note: addItemsToEvent dan deleteItemsFromEvent bisa dibuatkan decoratornya agar lebih hemat penulisan
    event = Event.objects.filter(id=pk)
    all_inventory_id = Inventory.objects.values_list('id', flat=True)
    
    if 'list_item' not in request.session:
        request.session['list_item'] = []
    
    id_items_in_event = Inventory.objects.filter(eventitems__events=pk).values_list('id', flat=True)
    print('id_items_in_event: ',id_items_in_event)
    if request.method == 'POST':
        item_id = request.POST.get('tambah-item-textfield')
        if request.POST.get('additem-to-event-button') and (item_id not in id_items_in_event) and (item_id in all_inventory_id):
            # Jika id yang dimasukkan belum ada di event dan ada di inventory, maka ditambahkan ke session
            request.session['list_item'].append(item_id)
        elif request.POST.get('save-button'):
            for i in request.session['list_item']:
                added_items = EventItems(
                    events_id = pk,
                    items_id = i,
                    status_in_event = 'Barang tersedia'
                )
                added_items.save()
            request.session.flush()
            return redirect('eventDetail', pk=pk)
        elif request.POST.get('cancel-button'):
            request.session.flush()
            return redirect('eventDetail', pk=pk)

    event_items = Inventory.objects.filter(id__in=request.session['list_item'])
    # session harus disave agar hasil modified tersimpan
    request.session.modified = True
    context = {
        'events':event,
        'event_items':event_items
    }
    return render(request, 'inventory_app/add-item-to-event.html', context=context)
    None

def deleteItemsFromEvent(request, pk):
    event = Event.objects.filter(id=pk)
    all_inventory_id = Inventory.objects.values_list('id', flat=True)
    
    if 'list_item' not in request.session:
        request.session['list_item'] = []
    
    id_items_in_event = Inventory.objects.filter(eventitems__events=pk).values_list('id', flat=True)
    print('id_items_in_event: ',id_items_in_event)
    if request.method == 'POST':
        item_id = request.POST.get('tambah-item-textfield')
        if request.POST.get('additem-to-event-button') and (item_id in id_items_in_event) and (item_id in all_inventory_id):
            # Jika id yang dimasukkan belum ada di event dan ada di inventory, maka ditambahkan ke session
            request.session['list_item'].append(item_id)
        elif request.POST.get('delete-button'):
            event_items = EventItems.objects.filter(events_id=pk, items_id__in=request.session['list_item'])
            print('{:^40}'.format(''))
            print('ids: ',request.session['list_item'])
            print('Event items before delete: ',event_items)
            event_items.delete()
            print('Event items after delete: ',event_items)
            print('{:^40}'.format(''))
            request.session.flush()
            return redirect('eventDetail', pk=pk)
        elif request.POST.get('cancel-button'):
            request.session.flush()
            return redirect('eventDetail', pk=pk)

    event_items = Inventory.objects.filter(id__in=request.session['list_item'])
    # session harus disave agar hasil modified tersimpan
    request.session.modified = True
    context = {
        'events':event,
        'event_items':event_items
    }
    return render(request, 'inventory_app/delete-item-from-event.html', context=context)
    None

def stockChecking(request, pk):
    if request.method == 'POST':
        update_to_tersedia = request.POST.get('tersediaText') # refer to form dengan method POST, dan ambil entity yang memiliki ID 'tersediaText'
        update_to_terjual = request.POST.get('terjualText') # refer to form dengan method POST, dan ambil entity yang memiliki ID 'terjualText'
        
        # kalau yang di check-in adalah Tersedia, maka update di EventItems dan Inventory
        if update_to_tersedia:
            EventItems.objects.filter(events=pk, items=update_to_tersedia).update(status_in_event='Barang tersedia') 
            Inventory.objects.filter(id=update_to_tersedia).update(item_last_status='Barang tersedia')
        # kalau yang di check-in adalah Terjual, maka update di EventItems dan Inventory
        elif update_to_terjual:
            EventItems.objects.filter(events=pk, items=update_to_terjual).update(status_in_event='Terjual')
            Inventory.objects.filter(id=update_to_terjual).update(item_last_status='Terjual')
    
    event_details = Inventory.objects.filter(eventitems__events=pk).annotate(items_status = F('eventitems__status_in_event')).order_by('eventitems__status_in_event', 'id') # query all items in inventory, dimana events id sama dengan pk yang dipassing (many to many relationship). Python memberikan kemudahan bagi developer untuk melakukan lookup dengan menggunakan *namaTabelLain*__*kolomTabelLainTersebut*. annotate menambahkan fields tertentu dari tabel lain.
    terjual_count = EventItems.objects.filter(status_in_event='Terjual', events=pk).count()
    barang_tersedia_count = EventItems.objects.filter(status_in_event='Barang tersedia', events=pk).count()
    barang_tidak_ada_count = EventItems.objects.filter(status_in_event='Barang tidak ada', events=pk).count()

    events = Event.objects.filter(id=pk)
    context = {'event_details':event_details, 
               'events':events, 
               'terjual_count':terjual_count,
               'barang_tersedia_count':barang_tersedia_count,
               'barang_tidak_ada_count':barang_tidak_ada_count,
               }
    return render(request, 'inventory_app/stock-checking.html', context=context)