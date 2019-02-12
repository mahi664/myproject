from django.shortcuts import render
from django.http import HttpResponse
from .models import MatchSchedule,mypredictions,pointtable,appearances,goals,assists,cleansheets
from django import forms
# Create your views here.
def index(request):
    ptstable = pointtable.objects.all()
    return HttpResponse(render(request,'index.html',{'ptstable':ptstable}))


def matches(request):
    if request.method=="POST":
        team = request.POST.get('team')
        mat = mypredictions.objects.filter(hometeam = team)
    else:
        mat = mypredictions.objects.all()
    context ={
        'mat':mat,
    }
    return  HttpResponse(render(request,'matches.html',context))

def predictresult(request):
    return HttpResponse(render(request,'prediction.html'))

def result(request):
    if request.method=='POST':
        hometeam = request.POST.get('hometeam')
        awayteam = request.POST.get('awayteam')
    return HttpResponse(awayteam)

def matchresult(request):
    if request.method=='POST':
        hometeam1 = request.POST.get('team1')
        awayteam1 = request.POST.get('team2')
        logo1 = request.POST.get('teamlogo1')
        logo2 = request.POST.get('teamlogo2')
        m = mypredictions.objects.all().filter(hometeam = hometeam1,awayteam = awayteam1)
        context={'hometeam' : hometeam1, 'awayteam' : awayteam1,'teamlogo1' : logo1, 'teamlogo2' : logo2 , 'winprob': m[0].winprobability , 'score':m[0].score}
    return HttpResponse(render(request,'matchresult.html',context))

def players(request):
    app = appearances.objects.all()
    goal = goals.objects.all()
    assist = assists.objects.all()
    cs = cleansheets.objects.all()
    return HttpResponse(render(request,'players.html',{'app':app,'goal':goal,'assist':assist,'cs':cs}))