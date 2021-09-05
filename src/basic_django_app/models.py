from django.db import models
from safedelete.config import DELETED_VISIBLE_BY_PK, SOFT_DELETE_CASCADE, NO_DELETE

from simple_history.models import HistoricalRecords
from safedelete.models import SafeDeleteModel, SOFT_DELETE

from safedelete.managers import SafeDeleteManager
class ModelManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

    def get_queryset(self):
        query_set = super(ModelManager, self).get_queryset()
        # Softdelete filter for many to many relationships
        if hasattr(self, "through") and hasattr(self, "source_field_name") and hasattr(self, "instance") and hasattr(self, "target_field_name"):
            through_qs = self.through.objects.filter(deleted__isnull=True, **{self.source_field_name + '_id':self.instance}).values_list(self.target_field_name, flat=True)
            query_set = query_set.filter(pk__in=through_qs)
        return query_set

class Entity(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    objects = ModelManager()

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True