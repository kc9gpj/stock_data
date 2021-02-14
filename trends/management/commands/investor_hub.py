import praw
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db.models import F

from trends.models import IHTickerWeights, Tickers, IHVersion
import keys

class Command(BaseCommand):

    def handle(self, *args, **options):
        driver_path = '/snap/bin/chromium.chromedriver'
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get("https://investorshub.advfn.com/boards/tcloud2.aspx")

        version, created = IHVersion.objects.get_or_create(
            id=1,
        )
        version.version += 1

        version.save()
        tickers = Tickers.objects.all()
        class_names = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
        soup = BeautifulSoup(driver.page_source)
        for class_name in class_names:
            for a in soup.findAll("a", {"class": class_name}):
                for ticker in tickers:
                    if a.getText() == ticker.symbol:
                        weight = class_name.replace('s', '')
                        hits, created = IHTickerWeights.objects.get_or_create(
                            tickers_id=ticker.id,
                            version=version.version,
                            weight=weight
                        )
        driver.quit()