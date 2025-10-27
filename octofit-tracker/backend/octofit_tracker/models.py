from djongo import models
from djongo.models import ObjectIdField

class Team(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', to_field='_id')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', to_field='_id')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard', to_field='_id')
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
