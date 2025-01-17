import requests

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()



def fetchStocksUnderSegment(segment):
    stocks = []
    # Your API Key
    API_KEY = os.getenv("FMP_API_KEY")

    # API Endpoint for Stock Screener
    url = f"https://financialmodelingprep.com/api/v3/stock-screener"
    params = {
        "sector": "Technology",  # Specify the sector
        "limit": 100,           # Number of results
        "apikey": API_KEY        # Your API key
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Print or process the data
        for stock in data:
            stocks.append(stock['symbol'])
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
    return stocks
