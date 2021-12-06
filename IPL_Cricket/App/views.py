from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from App.models import*
from .forms import*
import sweetify
import math

# Create your views here.
def home(request):
    player=Player.objects.all()
    

    return render(request,'home.html',{'data1':player})

def details(request,id):
    d=Player.objects.filter(team_id=id)
    return render(request,'details.html',{'d':d})

def search(request):
    s=request.GET.get('search')
    result=Team.objects.get(name=s)
    data=Player.objects.filter(team=result)
    
    return render(request,'search_results.html',{'data':data,'result':result})

def add_team(request):
    if request.method =="POST":
        form=AddTeam(request.POST ,request.FILES)
        if form.is_valid:
            form.save()
            sweetify.success(request,'You successfully added')
            return redirect(home)
    else:
        form=AddTeam()
        return render(request,'add_team.html',{'form':form})    


def add_player(request):
    if request.method =="POST":
        form=AddPlayer(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            sweetify.success(request,'You successfully added')
            return redirect(home)
        else:
             return render(request,'add_player.html',{'form':form})
    else:
        form=AddPlayer()
        return render(request,'add_player.html',{'form':form})    


