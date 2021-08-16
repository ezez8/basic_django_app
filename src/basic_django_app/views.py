from rest_framework import viewsets

from basic_django_app.filters import EntityFilter


class SafeDeleteViewSet(viewsets.ModelViewSet):
    filterset_class = EntityFilter
    