from django.db import models


class Team(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField(upload_to="icon/")

    def __str__(self):
        return self.name

class Player(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_fetch')
    fullname=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    is_playing=models.BooleanField(default=False)
    role=models.CharField(max_length=20)
    photo=models.ImageField(upload_to="photo/")

    def __unicode__(self):
        return self.team
    def __str__(self) -> str:
        return self.fullname


