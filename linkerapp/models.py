from django.db import models


# Create your models here.
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return "Id-" + str(self.team_id) + ":  " + self.team_name


