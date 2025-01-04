from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'index.html')

def matches (request):
    return render(request, 'matches.html')

def teams (request):
    return render(request, 'teams.html')

def points_table (request):
    return render(request, 'points_table.html')

def gallary (request):
    return render(request, 'gallary.html')

def contact (request):
    return render(request, 'contact.html')