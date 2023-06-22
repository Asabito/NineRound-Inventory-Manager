from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('new-event', views.newEvent, name='new-event'),
    path('event-detail/<str:pk>/', views.eventDetail, name='eventDetail'),
    path('event-detail/<str:pk>/add-items-to-event', views.addItemsToEvent, name='addItemsToEvent'),
    path('event-detail/<str:pk>/stock-checking', views.stockChecking, name='stockChecking'),
]