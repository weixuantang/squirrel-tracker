from django.shortcuts import render
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
