from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.showmap, name='showmap'),
    path('sightings', views.sightings, name='sightings')
]
