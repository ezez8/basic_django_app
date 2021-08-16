from django_filters import rest_framework as filters

from basic_django_app.models import Entity

class EntityFilter(filters.FilterSet):
    class Meta:
        model = Entity
        fields = ('created', 'updated', 'deleted')