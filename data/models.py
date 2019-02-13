import uuid
from django.db import models
from django.conf import settings

# DataSet Object
class DataSet(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    content = models.ImageField(upload_to='%Y/%m/%d/', max_length=100)
    release_datetime = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s %s" % (self.uuid, self.name, self.content, self.default)

