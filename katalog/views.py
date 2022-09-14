from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    data_barang_wishlist = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Ernest Benedictus',
        'NPM' : '2106751000',
    }
    return render(request, "katalog.html", context)



