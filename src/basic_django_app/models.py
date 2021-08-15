from django.db import models
from safedelete.config import DELETED_VISIBLE_BY_PK

from simple_history.models import HistoricalRecords
from safedelete.models import SafeDeleteModel, SOFT_DELETE

from safedelete.managers import SafeDeleteManager
class ModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class Entity(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    objects = ModelManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True