import re
import pytz
import datetime
from calendar import monthrange

from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse

from trends.models import Tickers, TickerHits, Version, IHTickerWeights, IHVersion


def reddit(request):
    version = Version.objects.all().first()
    range_version = version.version + 1
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits")[:50]
    print(ticker_hits)
    symbol = []
    hits = []
    sec_symbol = []
    sec_hits = []
    for i in reversed(range(range_version)):
        if i == 0:
            continue
        first_highest = TickerHits.objects.filter(version=i).order_by("-hits").first()
        if not first_highest:
            break
        symbol.append(str(first_highest.tickers.symbol))
        hits.append(str(first_highest.hits))
        sec_highest = TickerHits.objects.filter(version=i).order_by("-hits")[1:2].first()
        sec_symbol.append(str(sec_highest.tickers.symbol))
        sec_hits.append(str(sec_highest.hits))

    context = {
        'ticker_hits': ticker_hits,
        'symbol': symbol[::-1],
        'hits': hits[::-1],
        'sec_symbol': sec_symbol[::-1],
        'sec_hits': sec_hits[::-1]
    }

    return render(request, "trends/reddit.html", context)


def ihub(request):
    version = IHVersion.objects.all().first()
    ticker_weights = IHTickerWeights.objects.filter(version=version.version).order_by("-weight")[:20]

    context = {
        'ticker_weights': ticker_weights,
    }

    return render(request, "trends/ihub.html", context)
