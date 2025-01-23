from django.db import models
from django.core.exceptions import ValidationError
# from django.db import models

# Team Model
class Team(models.Model):
    name = models.CharField(max_length=100)
    captain_name = models.CharField(max_length=100)
    captain_phone_number = models.CharField(max_length=15)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Player Model
class Player(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name


# models.py
# models.py

class Match(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    ROUND_CHOICES = [
        ('Group Stage', 'Group Stage'),
        ('Quarterfinals', 'Quarterfinals'),
        ('Semifinals', 'Semifinals'),
        ('Final', 'Final'),
    ]

    team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_matches', null=True, blank=True)  # Allow null for bypass
    date = models.DateTimeField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_penalty = models.BooleanField(default=False)
    penalty_team1 = models.CharField(max_length=100, blank=True, null=True)
    penalty_team2 = models.CharField(max_length=100, blank=True, null=True)
    is_bypass = models.BooleanField(default=False)  # New field for bypass matches
    bypass_winner = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, related_name='bypass_winner')  # Winner in case of bypass

    round = models.CharField(max_length=20, choices=ROUND_CHOICES, default='Group Stage')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Upcoming')

    def clean(self):
        if self.is_penalty:
            if not self.penalty_team1 or not self.penalty_team2:
                raise ValidationError("Penalty data must be provided for both teams if penalties apply.")
            try:
                [int(score.strip()) for score in self.penalty_team1.strip("[]").split(',')]
                [int(score.strip()) for score in self.penalty_team2.strip("[]").split(',')]
            except ValueError:
                raise ValidationError("Penalty data must be a comma-separated list of integers.")
        else:
            self.penalty_team1 = None
            self.penalty_team2 = None

    def get_winner(self):
        if self.is_bypass:
            return self.bypass_winner.name if self.bypass_winner else "Bypass Winner Not Set"

        if not self.is_completed:
            return "Match not completed"

        def parse_penalty_scores(penalty_data):
            if not penalty_data:
                return []
            try:
                return [int(score.strip()) for score in penalty_data.strip("[]").split(',')]
            except ValueError:
                raise ValidationError(f"Invalid penalty data: {penalty_data}")

        penalty_team1_scores = parse_penalty_scores(self.penalty_team1)
        penalty_team2_scores = parse_penalty_scores(self.penalty_team2)

        team1_penalty_goals = sum(penalty_team1_scores)
        team2_penalty_goals = sum(penalty_team2_scores)

        total_team1_score = self.score_team1 + team1_penalty_goals
        total_team2_score = self.score_team2 + team2_penalty_goals

        if total_team1_score > total_team2_score:
            return self.team1.name
        elif total_team1_score < total_team2_score:
            return self.team2.name
        else:
            return "Draw"
