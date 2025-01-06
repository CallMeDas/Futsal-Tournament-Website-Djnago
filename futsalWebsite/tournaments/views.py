from django.shortcuts import render
from .models import Team, Match

# Create your views here.
def home (request):
    return render(request, 'index.html')

def matches(request):
    matches = Match.objects.all()
    for match in matches:
        # Split penalty data into lists if penalties exist
        if match.penalty_team1:
            match.penalty_team1 = match.penalty_team1.split(',')  # Split on commas
        if match.penalty_team2:
            match.penalty_team2 = match.penalty_team2.split(',')
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