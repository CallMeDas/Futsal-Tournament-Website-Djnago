from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('matches/', views.matches),
    path('teams/', views.teams),
    path('points_table/', views.points_table),
    path('gallary/', views.gallary),
    path('contact/', views.contact),
]
