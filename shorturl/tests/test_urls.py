from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shorturl.views import small_url, home


# Create your tests here.
# 

class TestUrls(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    #URL testing
    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
