import requests
import json 
from yahoo_fin import stock_info as si

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from trends.models import Tickers, TickerHits, Version, IHTickerWeights, IHVersion, Twitter

import keys



def index(request):

    version = Version.objects.all().first()
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits").first()
    reddit = ticker_hits.tickers.symbol
    # version = IHVersion.objects.all().first()
    # ticker_weights = IHTickerWeights.objects.filter(version=version.version).order_by("-weight").first()
    # ihub = ticker_weights.tickers.symbol

    twitter_tickers = Twitter.objects.all().order_by("-created_at").first()
    twitter = twitter_tickers.tickers.symbol
    
    reddit_data = si.get_quote_table(reddit, dict_result = True)
    print(reddit_data)
    print(reddit_data['Quote Price'])
    print(reddit_data['Volume'])
    print(reddit_data['Previous Close'])

    {'1y Target Est': 7.44, '52 Week Range': '2.70 - 28.77', 'Ask': '13.10 x 1800', 'Avg. Volume': 54455756.0, 'Beta (5Y Monthly)': 1.09, 'Bid': '13.00 x 1800', "Day's Range": '12.12 - 13.28', 'EPS (TTM)': -1.49, 'Earnings Date': nan, 'Ex-Dividend Date': nan, 'Forward Dividend & Yield': 'N/A (N/A)', 'Market Cap': '7.291B', 'Open': 12.29, 'PE Ratio (TTM)': nan, 'Previous Close': 12.46, 'Quote Price': 13.039999961853027, 'Volume': 17874672.0}

    context = {
        'reddit': reddit,
        'reddit_price': si.get_quote_table(reddit, dict_result = True),
        # 'ihub': ihub,
        'twitter': twitter,
        'twitter_price':si.get_live_price(twitter)
        
    }
    return render(request, "stock_data/screener.html", context)
