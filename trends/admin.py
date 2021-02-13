from django.contrib import admin

from .models import Tickers, TickerHits, Twitter, IHTickerWeights

admin.site.register(Tickers)
admin.site.register(TickerHits)
admin.site.register(Twitter)
admin.site.register(IHTickerWeights)