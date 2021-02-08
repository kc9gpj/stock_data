import praw
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db.models import F

from trends.models import TickerHits, Tickers, Version
import keys

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get('https://financialmodelingprep.com/api/v3/stock/actives?apikey={}'.format(keys.fmp_key))
        data = response.json()
        print(data)