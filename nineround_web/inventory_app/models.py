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
    



