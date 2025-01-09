from django.shortcuts import render
from .models import Team, Match
from collections import defaultdict

# Home View
def home(request):
    return render(request, 'index.html')

# Matches View
from collections import defaultdict  # Add this line
from django.shortcuts import render
from .models import Match

def matches(request):
    matches = Match.objects.all()
    for match in matches:
        # Parse penalties for each match
        match.penalty_team1_list = (
            match.penalty_team1.strip("[]").split(',') if match.penalty_team1 else []
        )
        match.penalty_team2_list = (
            match.penalty_team2.strip("[]").split(',') if match.penalty_team2 else []
        )
        match.winner = match.get_winner()  # Determine the winner
    return render(request, 'matches.html', {'matches': matches})



# Teams View
def teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})

# Points Table View
def points_table(request):
    teams = Team.objects.all().order_by('-points')  # Order teams by points (descending)
    return render(request, 'points_table.html', {'teams': teams})

# Gallery View
def gallary(request):
    return render(request, 'gallary.html')  # Corrected spelling of "gallery"

# Contact View
def contact(request):
    return render(request, 'contact.html')
