from django.shortcuts import render
from mywatchlist.models import WatchlistFilm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistFilm.objects.all()
    sudahDitonton = 0
    belumDitonton = 0
    pesan = ""
    for i in data_watchlist:
        if i.film_watched == True:
            sudahDitonton+=1
        else:
            belumDitonton+=1
    if sudahDitonton >= belumDitonton:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    context = {
    'watchlist_film': data_watchlist,
    'nama': 'Hikam Fajduani',
    'pesan': pesan
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchlistFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistFilm.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = WatchlistFilm.objects.filter(pk=id)
    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



    # Jika XML
    #return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")