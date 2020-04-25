from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    details = models.TextField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField()
    age = models.IntegerField()
    position_in_field = models.CharField(max_length=256,
                                         choices=(('1', 'حارس'), ('2', 'مدافع'), ('3', 'وسط'), ('4', 'مهاجم')))
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)


class GameScore(models.Model):
    first_team = models.CharField(max_length=256)
    second_team = models.CharField(max_length=256)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)
