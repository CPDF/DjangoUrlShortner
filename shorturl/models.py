from djongo import models
import uuid
from datetime import date

####

data_dict = {
    'type' : 'Date',
    'expireAfterSeconds' : '500',
}

# Create your models here.
class Url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    long = models.CharField(max_length=1000)
    short = models.CharField(max_length=10)
    created_at = models.DateField(default=date.today)
    verbose_name="urls"

    def __str__(self):
        return str(self.long)
