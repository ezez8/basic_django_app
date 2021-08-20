from django.contrib import admin
from basic_django_app.admin import EntityAdmin

from notifications.models import Notification

admin.site.register([Notification], EntityAdmin,)
