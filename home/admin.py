from django.contrib import admin
from .models import Home_barang
# Register your models here.

my_model = [Home_barang]
admin.site.register(my_model)