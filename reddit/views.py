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

from reddit.models import Tickers, TickerHits, Version  


def reddit(request):
    version = Version.objects.all().first()
    prev_version = version.version - 1
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits")[:20]
    
    symbol = []
    hits = []
    for i in range(version.version):
        print(i)
        if i == 0:
            continue
        highest = TickerHits.objects.filter(version=version.version).order_by("-hits").first()
        symbol.append(str(highest.tickers.symbol))
        hits.append(str(highest.hits))
        if version.version - 4 == i:
            break
    print(symbol)
    print(hits)
    context = {
        'ticker_hits': ticker_hits,
        'symbol': symbol,
        'hits': hits
    }

    return render(request, "reddit/reddit.html", context)


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
