from django.shortcuts import render
from .models import Team, Match
from collections import defaultdict

# Home View
def home(request):
    return render(request, 'index.html')

# Matches View
def matches(request):
    matches = Match.objects.all().order_by('date')
    grouped_matches = defaultdict(list)

    for match in matches:
        # Group matches by round
        grouped_matches[match.round].append(match)

        # Process penalties if they exist
        if match.penalty_team1:
            match.penalty_team1 = match.penalty_team1.split(',')
        if match.penalty_team2:
            match.penalty_team2 = match.penalty_team2.split(',')

    return render(request, 'matches.html', {'grouped_matches': grouped_matches})

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
