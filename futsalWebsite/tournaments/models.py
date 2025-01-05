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
    


from django.core.exceptions import ValidationError
from django.db import models

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    is_penalty = models.BooleanField(default=False)
    penalty_team1 = models.CharField(max_length=100, blank=True, null=True)  # Store penalties as a comma-separated string
    penalty_team2 = models.CharField(max_length=100, blank=True, null=True)

def clean(self):
    if self.is_penalty:
        for field_name in ['penalty_team1', 'penalty_team2']:
            field_value = getattr(self, field_name, '')
            # Remove quotes and extra spaces
            cleaned_value = field_value.replace('"', '').replace("'", "").strip()
            setattr(self, field_name, cleaned_value)
            
            # Ensure the penalties contain only 1s and 0s
            if not all(char in '10' for char in cleaned_value.replace(',', '')):
                raise ValidationError({field_name: 'Penalties should only contain 1s and 0s separated by commas.'})
    else:
        self.penalty_team1 = ''
        self.penalty_team2 = ''


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"

