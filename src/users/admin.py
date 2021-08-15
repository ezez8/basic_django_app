from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from basic_django_app.admin import EntityAdmin
from users.models import User

admin.site.register([User, ], EntityAdmin)