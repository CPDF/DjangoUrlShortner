from .models import Url


def my_cron_job():
    Url.objects.create(long="tesst")


