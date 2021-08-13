from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from movies.models import Participation, Film, Actor

# Register your models here.

admin.site.register([Participation, Actor, Film, ], SimpleHistoryAdmin)