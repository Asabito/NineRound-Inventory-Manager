from django.db import models

# Create your models here.
class Event(models.Model):
    nama = models.CharField(max_length=80)
    lokasi = models.CharField(max_length=250)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    status = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nama
    
class Items(models.Model):
    events = models.ManyToManyField(Event)
    nama = models.CharField(max_length=250)
    keterangan = models.CharField(max_length=250)
    ukuran_choices = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('All Size', 'All Size'),
    ]
    ukuran = models.CharField(max_length=8, choices=ukuran_choices, default='All Size')
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nama

