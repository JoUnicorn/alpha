from datetime import datetime
from django.shortcuts import render
import requests
import json

API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "MSFT",
    "apikey": "Q5I0WW1DQE5CBEQH",
}

response = requests.get(API_URL, params=data).json()

def stock(request):
    return render(request, 'visualization/stock.html', {'date': datetime.now(), 'stocks': response['Time Series (Daily)']})
