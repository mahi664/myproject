from django.db import models

# Create your models here.
class MatchSchedule(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    team1 = models.CharField(max_length=200)
    teamlogo1=models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    teamlogo2 = models.CharField(max_length=200)

class mypredictions(models.Model):
    hometeam = models.CharField(max_length=50)
    awayteam = models.CharField(max_length=50)
    winprobability = models.FloatField(default=0)
    score = models.CharField(max_length=255)

class pointtable(models.Model):
    club = models.CharField(max_length=100)
    matchplayed = models.IntegerField(default=0)
    matcheswon = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    matcheslost = models.IntegerField(default=0)
    goaldiff = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

class appearances(models.Model):
    name = models.CharField(max_length=100)
    appearance = models.IntegerField(default=0)

class goals(models.Model):
    name = models.CharField(max_length=100)
    goals = models.IntegerField(default=0)

class assists(models.Model):
    name = models.CharField(max_length=100)
    assist = models.IntegerField(default=0)

class cleansheets(models.Model):
    name = models.CharField(max_length=100)
    cs = models.IntegerField(default=0)