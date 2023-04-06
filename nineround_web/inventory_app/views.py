from django.shortcuts import render
from django.http import HttpResponse
from .models import Event # import models
from django.db.models import Q


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
    return render(request, 'inventory_app/event.html', context=context)
    # return HttpResponse('Home Page')

def eventDetail(request, pk):


    return render(request, 'inventory_app/event-detail.html', )