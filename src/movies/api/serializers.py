from rest_framework import serializers

from movies.models import Participation, Film, Actor

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['url', 'id', 'name', 'actors',]

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['url', 'id', 'name', 'films',]

class ParticipationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participation
        fields = ['url', 'id', 'name', 'film', 'actor',]