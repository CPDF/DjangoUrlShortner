#import environ
from pymongo import MongoClient
from datetime import timedelta, datetime
from django.utils.timezone import now
import environ

env = environ.Env()
environ.Env.read_env()


"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client = MongoClient()
try:
   # The ismaster command is cheap and does not require auth.
   client.admin.command('ismaster')
except ConnectionFailure:
   print("Server not available")
"""

time = datetime.now()
delete_date = (round(time.timestamp() * 1000))

delete_command = {"expire_at" : { "$lt" : delete_date } }
    

####

# env = environ.Env()
# environ.Env.read_env()

def connect_mongo():
    #connection = MongoClient(env("DJANGO_SECRET_KEY"))
    #Used the mongo client connection for python 3.4. Version 3.6 was bugged.
    client = MongoClient(env("DATABASE_SRV_APP"))
    db = client.urls2
    links_db = db.shorturl_url
    return links_db


def my_cron_job():
    mongo = connect_mongo()
    database = mongo
    database.delete_many(delete_command)
