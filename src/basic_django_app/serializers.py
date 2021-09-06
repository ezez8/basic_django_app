from rest_framework import serializers

from basic_django_app.models import Entity


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = ['url', 'id', 'created', 'updated', 'deleted',]
        abstract = True