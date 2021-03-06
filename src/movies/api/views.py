from rest_framework import viewsets
from movies.api.filters import FilmFilter
from movies.api.serializers import ParticipationSerializer, FilmSerializer, ActorSerializer

from movies.models import Participation, Film, Actor


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filterset_class = FilmFilter

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer