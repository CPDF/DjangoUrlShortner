from django.test import TestCase, Client
from django.urls import reverse
import json

from shorturl.views import small_url

class TestViews(TestCase):
    
    #Test individual function
    #Test if test_shorten_url returns a string type
    def test_shorten_url(self):
        actual = small_url()
        #expected = {"tank_a": ["rabbit"]}
        self.assertIsInstance(actual, str)

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        #self.xxx_url = reverse('xxx')

    def test_home_get(self):
        
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'url_page.html')


