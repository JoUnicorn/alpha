from datetime import datetime
from django.shortcuts import render, get_object_or_404
import requests
import json
from django.http import JsonResponse
from .models import Category_sector, Category_industry, Stock
from django.core import serializers

API_URL = "https://www.alphavantage.co/query"

def stock(request):
    return render(request, 'visualization/stock.html', {'date': datetime.now()})

def search_s(request):
    symbol = request.GET['symbol']

#    data = {
#        "function": "SYMBOL_SEARCH",
#        "keywords": symbol,
#        "apikey": "Q5I0WW1DQE5CBEQH",
#    }

#    response = requests.get(API_URL, params=data).json()

    response2 =Stock.objects.filter(symbol__startswith=symbol.upper()).order_by('symbol')
    stack=[]
    for data in response2:
        stack.append({'1. symbol':data.symbol, '2. name':data.company, 'sector':data.category_sector.sector, 'industry':data.category_industry.industry, 'exchange':data.exchange, 'ipo':data.ipoYear})

    data={
        'data':stack
    }

    print(data)

    return JsonResponse(data)

def return_s_data(request):
    symbol = request.GET['symbol']
    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": "Q5I0WW1DQE5CBEQH",
    }

    response = requests.get(API_URL, params=data).json()

    return JsonResponse(response['Time Series (Daily)'])
