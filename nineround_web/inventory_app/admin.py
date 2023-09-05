from django.contrib import admin

# Register your models here.
from .models import Event, Inventory
admin.site.register(Event)
admin.site.register(Inventory)