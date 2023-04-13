from django.db import models

# Create your models here.
    
class Inventory(models.Model):
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

class Event(models.Model):
    items = models.ManyToManyField(Inventory, through='EventItems')
    nama = models.CharField(max_length=80)
    lokasi = models.CharField(max_length=250)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    statusChoices = [
        ('Berlangsung', 'Berlangsung'),
        ('Selesai', 'Selesai'),
    ]
    status = models.CharField(max_length=11, choices=statusChoices, default='Berlangsung')

    def __str__(self) -> str:
        return self.nama
    
class EventItems(models.Model):
    events = models.ForeignKey(Event, on_delete=models.CASCADE)
    items = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    statusInEventChoices = [
        ('Terjual', 'Terjual'),
        ('Barang tersedia', 'Barang tersedia'),
        ('Barang tidak ada', 'Barang tidak ada'),
        ('Barang dalam event', 'Barang dalam event'),
    ]
    status_in_event = models.CharField(max_length=18, choices=statusInEventChoices, default='Barang tersedia')
