from django.contrib import admin

from movies.models import Participation, Film, Actor

# Register your models here.

admin.site.register([Participation, Actor, Film])
