from django.conf import settings
from django.db import models


class Auditable(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss", on_delete=models.PROTECT)

    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_related",
                                    related_query_name="%(app_label)s_%(class)ss_mod", on_delete=models.PROTECT)

    class Meta:
        abstract = True
