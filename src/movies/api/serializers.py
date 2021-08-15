from rest_framework import serializers

from movies.models import Participation, Film, Actor

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['url', 'id', 'name', 'actors', 'created', 'updated', 'deleted',]

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['url', 'id', 'name', 'films', 'created', 'updated', 'deleted',]

class ParticipationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participation
        fields = ['url', 'id', 'film', 'actor', 'created', 'updated', 'deleted',]