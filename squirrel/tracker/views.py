from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Squirrel
from django.db.models import Avg,Max,Min,Count,StdDev
from .forms import SquirrelForm, AddForm
# Create your views here.

def showmap(request):
    sightings = random.sample(list(Squirrel.objects.all()),100)
#    sightings = []
#    for temp in templist:
#        sightings.append({'latitude':temp.y, 'longitude': temp.x})
    context = {'sightings':sightings}
    return render(request,'tracker/map.html',context)

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tracker/sightings')
    else:
        form = AddForm()

    context ={
            'form': form,
    }
    return render(request,'tracker/edit.html',context)

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
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/tracker/sightings')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form':form,
        'squirrel':squirrel,
    }
    return render(request, 'tracker/edit.html', context)
