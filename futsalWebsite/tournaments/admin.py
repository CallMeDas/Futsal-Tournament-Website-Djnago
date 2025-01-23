from django.contrib import admin
from .models import Team, Player, Match

# Inline for Player in Team
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
    list_display = ('team1', 'team2', 'date', 'round', 'status', 'is_completed', 'is_penalty', 'is_bypass')
    fields = (
        'team1', 
        'team2', 
        'date', 
        'round', 
        'status', 
        'is_completed', 
        'is_penalty', 
        'score_team1',  
        'score_team2',  
        'penalty_team1', 
        'penalty_team2',
        'is_bypass',  # New field
        'bypass_winner'  # New field
    )

    def save_model(self, request, obj, form, change):
        try:
            if obj.is_penalty:
                [int(score.strip()) for score in obj.penalty_team1.strip("[]").split(',')]
                [int(score.strip()) for score in obj.penalty_team2.strip("[]").split(',')]
            super().save_model(request, obj, form, change)
        except ValueError:
            self.message_user(request, "Invalid penalty data format. Use comma-separated integers.", level="error")
