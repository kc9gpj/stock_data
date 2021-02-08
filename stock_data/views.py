import requests
import json 

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

import keys



def index(request):
    # response = requests.get('https://financialmodelingprep.com/api/v3/stock/actives?apikey={}'.format(keys.fmp_key))
    # data = response.json()
    # print(data)
    context = {
        
    }
    return render(request, "stock_data/screener.html", context)
