from django.db import models
from simple_history import register
from simple_history.models import HistoricalRecords

class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

class Film(Entity):
    name = models.CharField(max_length=50)
    actors = models.ManyToManyField(to='movies.actor', related_name='films', through='movies.participation')

class Actor(Entity):
    name = models.CharField(max_length=50)

class Participation(Entity):
    main_character = models.BooleanField(default=False)
    character_name = models.CharField(max_length=50, default='')
    film = models.ForeignKey(to='movies.film', on_delete=models.PROTECT, related_name='participations')
    actor = models.ForeignKey(to='movies.actor', on_delete=models.PROTECT, related_name='participations')