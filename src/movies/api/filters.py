from django_filters import rest_framework as filters

from movies.models import Film

class FilmFilter(filters.FilterSet):
    class Meta:
        model = Film
        fields = ('actors__name',)