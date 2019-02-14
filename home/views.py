from django.shortcuts import render, redirect
from .models import Home_barang
from .forms import PostForm

# Create your views here.
def home(request):
    home_barang = Home_barang.objects.all()
    return render(request, 'home/home.html', {'home_barangs': home_barang})

def input_barang(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'home/input_barang.html', {'form':form})

def barang_detail(request, barang_id):
    barang = Home_barang.objects.get(pk=barang_id)
    return render(request, 'home/barang_detail.html', {'barang':barang})