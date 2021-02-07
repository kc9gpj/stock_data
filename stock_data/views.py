import requests
import json 

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

import keys



def index(request):
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=SPX&apikey={}'.format(keys.api_key))
    data = response.json()
    context = {
    }
    return render(request, "stock_data/screener.html", context)
