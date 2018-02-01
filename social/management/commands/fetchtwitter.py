import oauth2
import requests
import datetime
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):


    def handle(self, *args, **options):
        query = "sachin tendulkar"
        date = datetime.datetime.now() - datetime.timedelta(days=7)
        url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + query + "&since=" + date
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""
        TOKEN = ""
        TOKEN_SECRET = ""
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=TOKEN, secret=TOKEN_SECRET)
        client = oauth2.Client(consumer, token)
        resp, content = client.request(url, method="GET", body="", headers='None')



