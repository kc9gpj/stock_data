import requests
import json 
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

    context = {
        'reddit': reddit,
        'ihub': ihub,
        'ihub_data': ihub_data,
        'twitter': twitter,
        'twitter_data': twitter_data,
        'reddit_data': reddit_data
        
    }
    return render(request, "stock_data/screener.html", context)
