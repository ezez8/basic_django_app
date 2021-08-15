from django.db import models

from basic_django_app.models import Entity

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