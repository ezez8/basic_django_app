from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

from movies.models import Participation, Film, Actor

class EntityAdmin(SimpleHistoryAdmin, SafeDeleteAdmin):
    list_display = (highlight_deleted,) + SafeDeleteAdmin.list_display

admin.site.register([Actor, Film, Participation], EntityAdmin)