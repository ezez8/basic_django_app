from django.contrib import admin
from basic_django_app.admin import EntityAdmin

from movies.models import Participation, Film, Actor

admin.site.register([Actor, Film, Participation], EntityAdmin)