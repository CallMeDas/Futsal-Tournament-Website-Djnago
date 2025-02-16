from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Match, Gallery
from collections import defaultdict
from django.contrib import messages
from .forms import ContactForm

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
            match.winner = match.get_winner()
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
    team = get_object_or_404(Team, team_slug=slug)
    return render(request, 'team_detail.html', {'team': team})

# Points Table View
def points_table(request):
    teams = Team.objects.all().order_by('-points') 
    return render(request, 'points_table.html', {'teams': teams})

# Gallery View
def gallery(request):
    images = Gallery.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})

# Contact View
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
