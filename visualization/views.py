from datetime import datetime
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

API_URL = "https://www.alphavantage.co/query"

def stock(request):
    return render(request, 'visualization/stock.html', {'date': datetime.now()})

def search_s(request):
    symbol = request.GET['symbol']
    data = {
        "function": "SYMBOL_SEARCH",
        "keywords": symbol,
        "apikey": "Q5I0WW1DQE5CBEQH",
    }

    response = requests.get(API_URL, params=data).json()

    return JsonResponse(response)

def return_s_data(request):
    symbol = request.GET['symbol']
    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": "Q5I0WW1DQE5CBEQH",
    }

    response = requests.get(API_URL, params=data).json()

    return JsonResponse(response['Time Series (Daily)'])
