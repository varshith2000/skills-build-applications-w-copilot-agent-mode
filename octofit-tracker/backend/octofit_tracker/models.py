from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()