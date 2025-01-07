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
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_penalty = models.BooleanField(default=False)
    penalty_team1 = models.CharField(max_length=100, blank=True, null=True)  # e.g., "1,0,1"
    penalty_team2 = models.CharField(max_length=100, blank=True, null=True)

    round = models.CharField(max_length=20, choices=ROUND_CHOICES, default='Group Stage')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Upcoming')  # New field

    def clean(self):
        if self.is_penalty:
            if not self.penalty_team1 or not self.penalty_team2:
                raise ValidationError("Penalty data must be provided for both teams if penalties apply.")
        else:
            self.penalty_team1 = None
            self.penalty_team2 = None

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date} ({self.round})"

def get_winner(self):
    # Ensure penalty fields are strings before splitting
    try:
        penalty_team1_scores = (
            [int(score) for score in self.penalty_team1.split(',')]
            if self.penalty_team1 else []
        )
    except ValueError:
        penalty_team1_scores = []

    try:
        penalty_team2_scores = (
            [int(score) for score in self.penalty_team2.split(',')]
            if self.penalty_team2 else []
        )
    except ValueError:
        penalty_team2_scores = []

    # Calculate total penalty goals
    team1_penalty_goals = sum(penalty_team1_scores)
    team2_penalty_goals = sum(penalty_team2_scores)

    # Determine the winner
    if self.score_team1 + team1_penalty_goals > self.score_team2 + team2_penalty_goals:
        return self.team1.name
    elif self.score_team1 + team1_penalty_goals < self.score_team2 + team2_penalty_goals:
        return self.team2.name
    else:
        return "Draw"
