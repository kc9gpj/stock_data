import re
import pytz
import datetime
from calendar import monthrange
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse

from trends.models import Tickers, TickerHits, Version, IHTickerWeights, IHVersion 


def reddit(request):
    version = Version.objects.all().first()
    range_version = version.version + 1
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits")[:40]
    print(ticker_hits)
    symbol = []
    hits = []
    for i in reversed(range(range_version)):
        if i == 0:
            continue
        highest = TickerHits.objects.filter(version=i).order_by("-hits").first()
        if not highest:
            break
        print(highest.tickers.symbol)
        symbol.append(str(highest.tickers.symbol))
        hits.append(str(highest.hits))
        if version.version - 4 == i:
            break

    context = {
        'ticker_hits': ticker_hits,
        'symbol': symbol[::-1],
        'hits': hits[::-1]
    }

    return render(request, "trends/reddit.html", context)


def ihub(request):
    version = IHVersion.objects.all().first()
    ticker_weights = IHTickerWeights.objects.filter(version=version.version).order_by("-weight")[:20]

    context = {
        'ticker_weights': ticker_weights,
    }

    return render(request, "trends/ihub.html", context)


def days_ago(days, dt=None):
    """
    Backdates a date by days
    """
    dt = datetime_or_now(dt)
    return dt - relativedelta(days=days)


def datetime_or_now(dt):
    if not dt:
        dt = timezone.now()
        dt = timezone.localtime(dt)
    elif isinstance(dt, datetime.date):
        tz = timezone.get_current_timezone()
        return tz.localize(datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0))
    return dt