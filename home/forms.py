from django import forms
from .models import Home_barang

class PostForm(forms.ModelForm):

    class Meta:
        model = Home_barang
        fields = ('nama', 'harga', 'deskripsi', 'picture')