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


# Match Model
class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_penalty = models.BooleanField(default=False)
    penalty_team1 = models.CharField(max_length=100, blank=True, null=True)  # Comma-separated 1s and 0s
    penalty_team2 = models.CharField(max_length=100, blank=True, null=True)

    def clean(self):
        if self.is_penalty:
            if not self.penalty_team1 or not self.penalty_team2:
                raise ValidationError("Penalty data for both teams is required when is_penalty is True.")
        else:
            self.penalty_team1 = None
            self.penalty_team2 = None

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"
