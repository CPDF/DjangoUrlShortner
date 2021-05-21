from django.test import TestCase, Client
from datetime import timedelta, datetime

from shorturl.models import Url

####

time = datetime.now()
expire_date = datetime.now() + timedelta(minutes=5)



class TestModels(TestCase):

    def setUp(self):
        self.url1 = Url.objects.create(
            id = 1,
            long = "https://petayuuchan.wordpress.com/2017/08/05/omen/",
            short = "AAAAA",
            created_at = time,
            expire_at = 1621456900909,
            ip = '127.0.0.1',
            domain = 'localhost',
            redirect_number = 1
        )


    def test_basic(self):
        self.assertEquals(self.url1.id, 1)