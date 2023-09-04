from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('new-event', views.newEvent, name='new-event'),
    path('event-detail/<str:pk>/', views.eventDetail, name='eventDetail'),
    path('event-detail/<str:pk>/add-items-to-event', views.addItemsToEvent, name='addItemsToEvent'),
    path('event-detail/<str:pk>/delete-items-from-event', views.deleteItemsFromEvent, name='deleteItemsFromEvent'),
    path('event-detail/<str:pk>/stock-checking', views.stockChecking, name='stockChecking'),
    path('inventory', views.inventoryPage, name='inventoryPage'),
    path('add-item-to-inventory', views.inventoryAddItem, name='inventoryAddItem'),
    path('delete-item-from-inventory', views.inventoryDeleteItem, name='inventoryDeleteItem'),
    path('barcode', views.barcodeGenerator, name='barcode'),
    path('barcode/download', views.downloadFile, name='barcode-download-url'),
]