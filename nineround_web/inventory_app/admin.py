from django.contrib import admin

# Register your models here.
from .models import Event, Items
admin.site.register(Event)
admin.site.register(Items)