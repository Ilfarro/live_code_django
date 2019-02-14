from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barang/tambah/', views.input_barang, name='input_barang'),
    path('<int:barang_id>', views.barang_detail, name='barang_detail'),
]