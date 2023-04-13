from django.contrib import admin

# Register your models here.
from .models import Event, Inventory, EventItems
admin.site.register(Event)
admin.site.register(Inventory)
admin.site.register(EventItems)