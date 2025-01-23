from django.shortcuts import render
from .models import Team, Match
from collections import defaultdict

# Home View
def home(request):
    return render(request, 'index.html')

# Matches View
from collections import defaultdict
from django.shortcuts import render
from .models import Match

# views.py

def matches(request):
    matches = Match.objects.all()
    for match in matches:
        if match.is_bypass:
            match.winner = match.get_winner()  # Bypass winner
        else:
            match.penalty_team1_list = (
                [penalty.strip() for penalty in match.penalty_team1.strip("[]").split(',')]
                if match.penalty_team1
                else []
            )
            match.penalty_team2_list = (
                [penalty.strip() for penalty in match.penalty_team2.strip("[]").split(',')]
                if match.penalty_team2
                else []
            )
            match.winner = match.get_winner()
    return render(request, 'matches.html', {'matches': matches})





# Teams View
def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})

# Points Table View
def points_table(request):
    teams = Team.objects.all().order_by('-points') 
    return render(request, 'points_table.html', {'teams': teams})

# Gallery View
def gallary(request):
    return render(request, 'gallary.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')
