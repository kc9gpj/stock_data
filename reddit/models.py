
from django.db import models


class Tickers(models.Model):
    symbol =  models.CharField(max_length=12)
    full_name = models.CharField(max_length=256)


class TickerHits(models.Model):
    tickers = models.ForeignKey(Tickers, related_name='ticker_hits', on_delete=models.CASCADE)
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField('creation date') 

