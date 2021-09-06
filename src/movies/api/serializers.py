from rest_framework import serializers
from basic_django_app.serializers import EntitySerializer

from movies.models import Participation, Film, Actor

class FilmSerializer(EntitySerializer):
    class Meta(EntitySerializer.Meta):
        model = Film
        fields = EntitySerializer.Meta.fields + [
            'name', 
            'actors',
        ]

class ActorSerializer(EntitySerializer):
    class Meta(EntitySerializer.Meta):
        model = Actor
        fields = EntitySerializer.Meta.fields + [
            'name', 
            'films',
        ]

class ParticipationSerializer(EntitySerializer):
    class Meta(EntitySerializer.Meta):
        model = Participation
        fields = EntitySerializer.Meta.fields + [
            'film', 
            'actor',
        ]