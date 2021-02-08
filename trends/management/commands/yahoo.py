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
        # tickers = Tickers.objects.all()
        # for ticker in tickers:
        #     response = requests.get('https://finance.yahoo.com/quote/FB/community?p=FB')
        #     print(response.json())

        #     break

        driver_path = '/usr/lib/chromium-browser/chromedriver'
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get("https://finance.yahoo.com/quote/FB/community?p=FB")
        print(driver.page_source)
        driver.quit()
        