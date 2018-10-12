from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
import requests
import json
from django.http import JsonResponse
from .models import Category_sector, Category_industry, Stock, Stock_daily
from django.core import serializers

API_URL = "https://www.alphavantage.co/query"

def stock(request):
    return render(request, 'visualization/stock.html', {'date': datetime.now(), 'vue': 'stock'})

def data_update(request):
    return render(request, 'visualization/data_update.html', {'date': datetime.now(), 'vue': 'data'})

def data_load(request):
    return render(request, 'visualization/data_load.html', {'date': datetime.now(), 'vue': 'data'})

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

    return JsonResponse(data)

def return_s_data(request):
    symbol = request.GET['symbol']
    response2 =Stock_daily.objects.filter(symbol=symbol.upper()).order_by('symbol')

    stack={}
    for data in response2:
        stack[data.date.strftime("%Y-%m-%d")]={'1. open':data.open, '2. high':data.high, '3. low':data.low, '4. close':data.close, '5. volume':data.volume}

    data=stack

    return JsonResponse(data)

def update_data(request):
    response2 =Stock.objects.all()

    for symbol in response2:
        x=Stock_daily.objects.filter(symbol=symbol.symbol.upper()).exists()
        if x:
            x=Stock_daily.objects.filter(symbol=symbol.symbol.upper()).latest('date')
            d=datetime.now()
            d0 = date(x.date.year,x.date.month, x.date.day)
            d1 = date(d.year,d.month, d.day)
            delta = d1 - d0

            if delta.days>1:
                data = {
                    "function": "TIME_SERIES_DAILY",
                    "symbol": symbol,
                    "outputsize": "compact", #compact for 100 quotes only
                    "apikey": "Q5I0WW1DQE5CBEQH",
                }

                response = requests.get(API_URL, params=data).json()
                data={'status':'Data updated'}
                for key, val in response['Time Series (Daily)'].items():
                    d=datetime.strptime(key, "%Y-%m-%d").date()
                    d1 = date(d.year,d.month, d.day)
                    delta2 = d1 - d0
                    if delta2.days>0:
                        Stock_daily(date=key, symbol=symbol, open=val["1. open"], high=val["2. high"], low=val["3. low"], close= val["4. close"], volume=val["5. volume"]).save()
                    else:
                        break

    data={'status':'Data up to date'}


    return JsonResponse(data)

def load_data(request):
    response2 =Stock.objects.all()

    for symbol in response2:
        x=Stock_daily.objects.filter(symbol=symbol.symbol.upper()).exists()
        if not x:
            data = {
                "function": "TIME_SERIES_DAILY",
                "symbol": symbol,
                "outputsize": "full", #compact for 100 quotes only
                "apikey": "Q5I0WW1DQE5CBEQH",
            }

            response = requests.get(API_URL, params=data).json()
            data=response['Time Series (Daily)']
            for key, val in response['Time Series (Daily)'].items():
                Stock_daily(date=key, symbol=symbol, open=val["1. open"], high=val["2. high"], low=val["3. low"], close= val["4. close"], volume=val["5. volume"]).save()

    data={'status':'Data loaded'}

    return JsonResponse(data)
