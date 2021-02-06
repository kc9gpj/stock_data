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

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def reddit(request):
    version = Version.objects.all().first()
    prev_version = version.version - 1
    print(prev_version)
    ticker_hits = TickerHits.objects.filter(version=version.version).order_by("-hits")[:20]
    context = {
        'ticker_hits': ticker_hits
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
