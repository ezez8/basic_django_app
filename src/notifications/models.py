from django.db import models

from basic_django_app.models import Entity

class Notification(Entity):
    title = models.CharField(max_length=100)
    message = models.TextField()

    to = models.ForeignKey(to='users.user', on_delete=models.PROTECT, related_name='notifications')
