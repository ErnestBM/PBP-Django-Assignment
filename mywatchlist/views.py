from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def status(request):
    list_film = MyWatchlist.objects.all()
    val = 0
    for film in list_film:
        if film.watched == "Yes":
            val += 1
    
    if val >= len(list_film) - val:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"


def show_watchlist(request):
    list_film = MyWatchlist.objects.all()
    context = {
        'list_film': list_film,
        'nama': 'Ernest Benedictus',
        'NPM' : '2106751000',
        'info' : status(request),
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




