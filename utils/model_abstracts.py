import uuid
from django.db import models


class Model(models.Model):
    """
    An abstract base class model that provides a UUID primary key field
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True