from rest_framework.response import Response
from rest_framework.views import APIView
import random
import string
import re

from datetime import timedelta, datetime


from shorturl.models import Url
from shorturl.serializers import PostSerializer

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        return rand_letters

def get_domain(req):
    domain = str(req)
    domain = re.search('https?://([A-Za-z_0-9.-]+).*', domain)
    if domain:
        return domain.group(1)

    return domain

def get_count():
    obj= Url.objects.last()    
    if(obj == None):
        return 1
    else:
        obj = obj.redirect_number
        return obj + 1

class GetView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Url.objects.all()
        post = qs.first()
        serializer = PostSerializer(post)
        return Response(serializer.data) 

class PostUrl(APIView):
    def post(self, request, *args, **kwargs):
        entry = Url()
        #get user data from form
        url_recieved = str(request.query_params['url'])
        #analytics
        domain = get_domain(request.query_params['url'])
        short_url = shorten_url()
        entry.ip = 0
        entry.domain = domain
        entry.long = url_recieved
        entry.short = short_url
        entry.redirect_number = get_count()
        entry.save()
        return Response('http://127.0.0.1:8000/' + short_url) 