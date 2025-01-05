from django.contrib import admin
from .models import Team, Player, Match
# Register your models here.

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1 


# Team Admin
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain_name')
    search_fields = ('name', 'captain_name')
    inlines = [PlayerInline]

# Player Admin
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'team')
    search_fields = ('name', 'team') 
    list_filter = ('team',)

# Match Admin
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'date', 'is_completed', 'is_penalty')
    fields = ('team1', 'team2', 'date', 'is_penalty', 'is_completed', 'penalty_team1', 'penalty_team2')

    actions = ['start_penalty_shootout']
