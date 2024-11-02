import yfinance as yf



def getData(ticker):
    tickInfo = yf.Ticker(ticker)
    hist = tickInfo.history(period="1mo")
    return hist

