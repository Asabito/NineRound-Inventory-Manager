from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # NEW
    # class Role(models.TextChoices):
    #     SUPERADMIN = "Superadmin", "Superadmin" 
    #     ADMIN = "Admin", "Admin"
    #     GUEST = "Guest", "Guest"
    roleChoices = [
        ("Superadmin", "Superadmin"),
        ("Admin", "Admin"),
        ("Guest", "Guest"),
    ]
    role = models.CharField(max_length=12, choices=roleChoices, default="Guest")


class Event(models.Model):
    nama = models.CharField(max_length=80)
    lokasi = models.TextField(max_length=300)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField()
    statusChoices = [
        ('Berlangsung', 'Berlangsung'),
        ('Selesai', 'Selesai'),
    ]
    status = models.CharField(max_length=11, choices=statusChoices, default='Berlangsung')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.nama
    

class Inventory(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
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
    # ukuran = models.CharField(max_length=8, choices=ukuran_choices, default='All Size')
    ukuran = models.CharField(max_length=9)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    itemLastStatusChoices = [
        ('Terjual', 'Terjual'),
        ('Tersedia', 'Tersedia'),
        ('Tidak ada', 'Tidak ada'),
    ]
    item_last_status = models.CharField(max_length=18, choices=itemLastStatusChoices, default='Tersedia')
    items_event_location = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nama
    



# class EventItems(models.Model):
#     # gunakan Class Meta untuk melakukan setting sesuai terhadap model yang dibuat, pilihan setting tersedia oleh Django
#     class Meta:
#         # gunakan unique_together untuk membuat Composite Key (tr table dengan 2 kolom sebagai PK)
#         unique_together = (('events','items'),)
#     events = models.ForeignKey(Event, on_delete=models.CASCADE)
#     items = models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     statusInEventChoices = [
#         ('Terjual', 'Terjual'),
#         ('Barang tersedia', 'Barang tersedia'),
#         ('Barang tidak ada', 'Barang tidak ada'),
#         ('Barang dalam event', 'Barang dalam event'),
#     ]
#     status_in_event = models.CharField(max_length=18, choices=statusInEventChoices, default='Barang tersedia')
