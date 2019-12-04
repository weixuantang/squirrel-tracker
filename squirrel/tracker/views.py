from django.shortcuts import render, get_object_or_404
import random
from .models import Squirrel
# Create your views here.
def showmap(request):
    templist = random.sample(list(Squirrel.objects.all()),100)
    sightings = []
    for temp in templist:
        sightings.append({'latitude':temp.y, 'longitude': temp.x})
    context = {'sightings':sightings}
    return render(request,'tracker/map.html',context)


def sightings(request):
    sightings = Squirrel.objects.order_by('unique_squirrel_id')
    context = {'sightings':sightings}
    return render(request, 'tracker/sightings.html', context)

