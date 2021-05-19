import uuid
from djongo import models
from django.utils.timezone import now
from datetime import timedelta, datetime


####

time = datetime.now()
expire_date = datetime.now() + timedelta(minutes=5)
expire_date_milliseconds = (round(expire_date.timestamp() * 1000))



# Create your models here.
class Url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    long = models.CharField(default='', max_length=1000)
    short = models.CharField(default='', max_length=10)
    created_at = models.DateTimeField(default=now)
    expire_at = models.IntegerField(default=expire_date_milliseconds)
    ip = models.CharField(default='', max_length=100)
    domain = models.CharField(default='', max_length=100)
    redirect_number = models.IntegerField(default=0)
    verbose_name="urls"


    def __str__(self):
        return self.long

