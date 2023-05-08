from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Inventory, EventItems # import models
from django.db.models import Q, F


# events = [
#     {'id':1, 'nama': 'event 1', 'lokasi':'kokas', 'tanggal_mulai':'12 Maret 2023', 'tanggal_berakhir':'19 Maret 2023', 'status':'Selesai'},
#     {'id':2, 'nama': 'event 2', 'lokasi':'JCC', 'tanggal_mulai':'21 Maret 2023', 'tanggal_berakhir':'27 Maret 2023', 'status':'Selesai'},
#     {'id':3, 'nama': 'event 3', 'lokasi':'pim', 'tanggal_mulai':'29 Maret 2023', 'tanggal_berakhir':'4 April 2023', 'status':'Berlangsung'},
# ]

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
    print('context ===== ',context)

    return render(request, 'inventory_app/event.html', context=context)
    # return HttpResponse('Home Page')

def eventDetail(request, pk):
    event_details = Inventory.objects.filter(eventitems__events=pk) # query all items in Inventory, dimana events id sama dengan pk yang dipassing (many to many relationship). Python memberikan kemudahan bagi developer untuk melakukan lookup dengan menggunakan *namaTabelLain*__*kolomTabelLainTersebut*
    events = Event.objects.filter(id=pk)
    context = {'event_details':event_details, 'events':events}
    # print('context ===== ',context)

    return render(request, 'inventory_app/event-detail.html', context=context)

def stockChecking(request, pk):
    if request.method == 'POST':
        update_to_tersedia = request.POST.get('tersediaText') # refer to form dengan method POST, dan ambil entity yang memiliki ID 'tersediaText'
        update_to_laku = request.POST.get('lakuText') # refer to form dengan method POST, dan ambil entity yang memiliki ID 'lakuText'

        EventItems.objects.filter(events=pk, items=update_to_tersedia).update(status_in_event='Barang tersedia') if update_to_tersedia else None
        EventItems.objects.filter(events=pk, items=update_to_laku).update(status_in_event='Terjual') if update_to_laku else None
    event_details = Inventory.objects.filter(eventitems__events=pk).annotate(items_status = F('eventitems__status_in_event')) # query all items in inventory, dimana events id sama dengan pk yang dipassing (many to many relationship). Python memberikan kemudahan bagi developer untuk melakukan lookup dengan menggunakan *namaTabelLain*__*kolomTabelLainTersebut*. annotate menambahkan fields tertentu dari tabel lain.

    events = Event.objects.filter(id=pk)
    context = {'event_details':event_details, 'events':events}
    return render(request, 'inventory_app/stock-checking.html', context=context)