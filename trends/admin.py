from django.contrib import admin

from .models import Tickers, TickerHits, Twitter, IHTickerWeights, IHVersion, Version

admin.site.register(Tickers)
admin.site.register(Version)
admin.site.register(TickerHits)
admin.site.register(Twitter)
admin.site.register(IHVersion)
admin.site.register(IHTickerWeights)