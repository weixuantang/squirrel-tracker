from django.shortcuts import render, get_object_or_404
import random
from .models import Squirrel
from django.db.models import Avg,Max,Min,Count,StdDev
from .forms import SquirrelForm
from django.http import HttpResponseRedirect
# Create your views here.

def showmap(request):
    templist = random.sample(list(Squirrel.objects.all()),100)
    sightings = []
    for temp in templist:
        sightings.append({'latitude':temp.y, 'longitude': temp.x})
    context = {'sightings':sightings}
    return render(request,'tracker/map.html',context)

def add(request):
    return render(request,"tracker/add.html")
    #remember to add a new Squirrel Object and write the template!
    
def added(request):
    return "Successfully added!"
    #need a html template, does not necessarily use this one

def showstats(request):
    dictlist = [Squirrel.objects.aggregate(num_of_squirrels = Count('unique_squirrel_id')),
            Squirrel.objects.aggregate(max_longitude = Max('x')),
            Squirrel.objects.aggregate(min_longitude = Min('x')),
            Squirrel.objects.aggregate(max_latitude = Max('y')),
            Squirrel.objects.aggregate(min_latitude = Min('y')),
            Squirrel.objects.filter(age ='Adult').aggregate(num_of_adults = Count('unique_squirrel_id')),
            Squirrel.objects.filter(running = True).aggregate(num_of_running_squirrels = Count('unique_squirrel_id')),
            Squirrel.objects.filter(eating = True).aggregate(num_of_eating_squirrels = Count('unique_squirrel_id')),
            Squirrel.objects.filter(climbing = True).aggregate(num_of_climbing_squirrels = Count('unique_squirrel_id'))]
    statslist = []
    for i in dictlist:
        statslist.append([list(i.keys())[0],list(i.values())[0]])     
    statsdict = {'stats':statslist}
    return render(request,'tracker/stats.html',statsdict)

def sightings(request):
    sightings = Squirrel.objects.order_by('unique_squirrel_id')
    context = {'sightings':sightings}
    return render(request, 'tracker/sightings.html', context)

def edit(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(instance=squirrel,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tracker/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    return render(request, 'tracker/edit.html', {'form':form,'squirrel':squirrel})
