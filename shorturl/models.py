from djongo import models
import uuid

# Create your models here.
class Url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    long = models.CharField(max_length=1000)
    short = models.CharField(max_length=10)
    verbose_name="urls"

    def __str__(self):
        return str(self.long)
