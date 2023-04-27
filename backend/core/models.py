from django.db import models


class Create(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class CreateUpdater(Create):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(Create.Meta):
        abstract = True
        ordering = ('-updated_at',)
