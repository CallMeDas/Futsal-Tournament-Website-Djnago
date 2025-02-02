from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('matches/', views.matches),
    path('teams/', views.teams_list, name="teams_list"),  # New path for listing all teams
    path('teams/<slug:slug>/', views.teams, name="team_detail"),  # Keep the detailed team view
    path('points_table/', views.points_table),
    path('gallary/', views.gallary),
    path('contact/', views.contact),
]
