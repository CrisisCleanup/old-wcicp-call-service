from django.db import models
import uuid


class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'calls'

    def __str__(self):
        return str(self.name)
