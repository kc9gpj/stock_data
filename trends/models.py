
from django.db import models


class Tickers(models.Model):
    symbol = models.CharField(max_length=12)
    full_name = models.CharField(max_length=256)


class TickerHits(models.Model):
    tickers = models.ForeignKey(Tickers, related_name='ticker_hits', on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    hits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class Version(models.Model):
    version = models.IntegerField(default=1)



class IHTickerWeights(models.Model):
    tickers = models.ForeignKey(Tickers, related_name='ih_ticker_weights', on_delete=models.CASCADE)
    version = models.IntegerField(default=1)
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class IHVersion(models.Model):
    version = models.IntegerField(default=1)
