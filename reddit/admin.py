from django.contrib import admin

from .models import Tickers, TickerHits

admin.site.register(Tickers)
admin.site.register(TickerHits)