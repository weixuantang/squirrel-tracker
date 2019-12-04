from django.urls import path
from . import views

urlpatterns = [
        path('map/',views.showmap, name='showmap'),
        path('sightings/add',views.add, name='add'),
        path('sightings/added',views.added, name='added'),#temporary setting
        path('sightings/stats',views.showstats, name='showstats'),
        ]
