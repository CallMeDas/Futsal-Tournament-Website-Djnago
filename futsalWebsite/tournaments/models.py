from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    captain_name = models.CharField(max_length=100)
    captain_phone_number = models.CharField(max_length=15)
    points = models.IntegerField(default=0) 

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name
    


class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_penalty = models.BooleanField(default=False)
    penalty_team1 = models.JSONField(default=list)
    penalty_team2 = models.JSONField(default=list)