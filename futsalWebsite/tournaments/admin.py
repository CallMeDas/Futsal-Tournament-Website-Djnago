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
    list_display = ('team1', 'team2', 'date', 'round', 'status', 'is_completed', 'is_penalty')
    fields = (
        'team1', 
        'team2', 
        'date', 
        'round', 
        'status', 
        'is_completed', 
        'is_penalty', 
        'score_team1',  # Include this field
        'score_team2',  # Include this field
        'penalty_team1', 
        'penalty_team2'
    )
    def save_model(self, request, obj, form, change):
        if obj.is_penalty:
            if not obj.penalty_team1 or not obj.penalty_team2:
                self.message_user(request, "Penalty details are required for both teams.", level="error")
        super().save_model(request, obj, form, change)
