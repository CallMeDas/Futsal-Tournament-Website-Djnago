from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('matches/', views.matches),
    path('teams/', views.teams_list, name="teams_list"),  
    path('teams/<slug:slug>/', views.teams, name="team_detail"),  
    path('points_table/', views.points_table),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
]
