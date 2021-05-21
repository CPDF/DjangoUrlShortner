from django.conf.urls import url
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Url
import random
import string
import re

from datetime import timedelta, datetime

#Warning! Use only if you wish to delete all objects: Url.objects.all().delete()


# Create your views here.

def small_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        return rand_letters

def get_domain(req):
    domain = str(req.POST["nm"])
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

def home(req):

    if(req.POST):
        #Use the Url model
        entry = Url()

        #get user data from form
        url_recieved = str(req.POST["nm"])
        #analytics
        domain = get_domain(req)
        

        #If custom shorten then custom else short_url
            #if custom shorten is already on database send error message
        if(len(str(req.POST["user_short"])) > 0):
            if(Url.objects.filter(short=str(req.POST["user_short"])).first()):
                messages.error(req, 'Short url already exist!')
                return redirect("/")
            else:
                short_url = str(req.POST["user_short"])

        #If a custom short url is not provided use the small_url function
        else:
            short_url = small_url()

        entry.ip = req.META['HTTP_ORIGIN']
        entry.domain = domain
        entry.long = url_recieved
        entry.short = short_url
        entry.redirect_number = get_count()
        entry.save()
        return redirect("display_short_url", short_url)

    return render(req, 'url_page.html')

def redirection(request, short_url):
    long_url = Url.objects.filter(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return HttpResponse('<h1>Link does not longer exists.</h1>')

def display_short_url(request, url):
    return render(request, 'short_url.html', context={"short_url_display": url})

def display_all(request):
    entry = Url.objects.all()
    context = {}
    for value in entry:
        context[value.short] = value.long

    return render(request, 'all_urls.html', {'values': context})