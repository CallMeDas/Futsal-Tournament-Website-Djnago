from django.shortcuts import render, get_object_or_404
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
# View for listing all teams
def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})

# View for individual team details
def teams(request, slug):
    team = get_object_or_404(Team, team_slug=slug)  # Fetch team by slug
    return render(request, 'team_detail.html', {'team': team})

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
