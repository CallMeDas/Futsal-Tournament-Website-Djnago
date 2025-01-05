from django.shortcuts import render
from .models import Team, Match

# Create your views here.
def home (request):
    return render(request, 'index.html')

def matches (request):
    matches = Match.objects.all()
    return render(request, 'matches.html', {'matches': matches})

def teams (request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams} )

def points_table (request):
    return render(request, 'points_table.html')

def gallary (request):
    return render(request, 'gallary.html')

def contact (request):
    return render(request, 'contact.html')