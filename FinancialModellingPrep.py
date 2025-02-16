import requests

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("FMP_API_KEY")


def fetchAllSegments():
    segments = []
    # API Endpoint for Stock Screener
    url = f"https://financialmodelingprep.com/api/v3/sectors-list"
    params = {
        "apikey": API_KEY        # Your API key
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Print or process the data
        for stock in data:
            segments.append(stock)
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
    return segments


def fetchStocksUnderSegment(segment):
    stocks = []
    # API Endpoint for Stock Screener
    url = f"https://financialmodelingprep.com/api/v3/stock-screener"
    params = {
        "sector": segment,  # Specify the sector
        "limit": 20,           # Number of results
        "apikey": API_KEY        # Your API key
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Print or process the data
        for stock in data:
            if stock['exchangeShortName'] == 'NYSE' or stock['exchangeShortName'] == 'NASDAQ':
                stocks.append(stock['symbol'])
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
    return stocks



def fetchFinancial(stock):
    data=''
    # API Endpoint for Stock Screener
    url = f"https://financialmodelingprep.com/api/v3/income-statement/"+stock
    params = {
        "apikey": API_KEY,        # Your API key
        "period": 'annual'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Print or process the data
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
    if data != '':
        return data
    else:
        return None
