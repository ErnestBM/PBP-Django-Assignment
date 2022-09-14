from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()


from django.db import models

class BarangKatalog(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()