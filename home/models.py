from django.db import models
from django.utils import timezone 

class Home_barang(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.TextField(max_length=255)
    picture = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama