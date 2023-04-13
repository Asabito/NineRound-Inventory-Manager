from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('event-detail/<str:pk>/', views.eventDetail, name='eventDetail'),
    path('event-detail/<str:pk>/stock-checking', views.stockChecking, name='stockChecking'),
]