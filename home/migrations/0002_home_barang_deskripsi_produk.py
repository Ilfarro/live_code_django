# Generated by Django 2.1.7 on 2019-02-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_barang',
            name='deskripsi_produk',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
