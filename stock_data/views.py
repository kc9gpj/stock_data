import requests
import json 
import datetime
from datetime import timedelta, date
from yahoo_fin import stock_info as si

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from trends.models import Tickers, TickerHits, Version, IHTickerWeights, IHVersion, Twitter


def index(request):

    version = Version.objects.all().first()
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits").first()
    reddit = ticker_hits.tickers.symbol
    version = IHVersion.objects.all().first()
    ticker_weights = IHTickerWeights.objects.filter(version=version.version).order_by("-weight").first()
    ihub = ticker_weights.tickers.symbol

    twitter_tickers = Twitter.objects.all().order_by("-created_at").first()
    twitter = twitter_tickers.tickers.symbol
    
    reddit_data = si.get_quote_table(reddit, dict_result = True)
    twitter_data = si.get_quote_table(twitter, dict_result = True)
    ihub_data = si.get_quote_table(ihub, dict_result = True)

    now = datetime.datetime.now()
    then = start_date = datetime.datetime.now() - datetime.timedelta(30)
    month_data = si.get_data(reddit, then, now)
    open_data = []
    for data in month_data.open:
        open_data.append(data)
    start_dt = date(2019,1,21)
    end_dt = date(2019,2,4)

    data_date = []
    weekdays = [5,6]
    for dt in daterange(then, now):
        if dt.weekday() not in weekdays:
            data_date.append(dt.strftime(str("%m-%d")))

    context = {
        'reddit': reddit,
        'ihub': ihub,
        'ihub_data': ihub_data,
        'twitter': twitter,
        'twitter_data': twitter_data,
        'reddit_data': reddit_data,
        'open_data': open_data,
        'data_date': data_date,
        
    }
    return render(request, "stock_data/screener.html", context)


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)