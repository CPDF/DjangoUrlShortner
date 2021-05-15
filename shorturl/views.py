from django.conf.urls import url
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Url
import random
import string



# Create your views here.
def index(req):
    return render(req, "index.html")

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        return rand_letters

def home(req):
    if(req.POST):
        entry = Url()
        url_recieved = str(req.POST["nm"])
        #If custom shorten then custom else short_url
            #if custom shorten is already on database send error message
        if(len(str(req.POST["user_short"])) > 0):
            if(Url.objects.filter(short=str(req.POST["user_short"])).first()):
                messages.error(req, 'Short url already exist!')
                return redirect("/")
            else:
                short_url = str(req.POST["user_short"])

        #If a custom short url is not provided use the shorten_url function
        else:
            short_url = shorten_url()

        entry.long = url_recieved
        entry.short = short_url
        entry.save()
        return redirect("display_short_url", short_url)

    return render(req, 'url_page.html')

def redirection(request, short_url):
    long_url = Url.objects.filter(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>Url doesnt exist</h1>'

def display_short_url(request, url):
    return render(request, 'short_url.html', context={"short_url_display": url})

def display_all(request):
    entry = Url.objects.all()
    context = {}
    for value in entry:
        context[value.short] = value.long

    return render(request, 'all_urls.html', {'values': context})