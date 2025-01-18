import yfinance as yf
import requests_cache
import pandas as pd
session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'


def getData(ticker):
    tickInfo = yf.Ticker(ticker,session=session)
    hist = tickInfo.history(period="1mo")
    print(hist)
    return hist

def getClosePrice(ticker,start_date,end_date):
    getInfo = yf.download(ticker,start_date,end_date,session=session)
    return getInfo["Close"]

def getSMA(ticker,movingAverage:int,start_date,end_date):
    getInfo = yf.download(ticker,start_date,end_date,session=session)
    getInfo["SMA"] = getInfo["Close"].rolling(window=movingAverage).mean()
    return getInfo["SMA"]

def getVolume(ticker,start_date,end_date):
    getInfo = yf.download(ticker,start_date,end_date,session=session)
    return getInfo["Volume"]

def getRSI(ticker,start_date,end_date,window):
    getInfo = yf.download(ticker,start_date,end_date,session=session)
    delta = getInfo['Close'].diff(1).dropna()
    loss = delta.copy()
    gains = delta.copy()

    gains[gains < 0] = 0
    loss[loss > 0] = 0
    #In following variables we are calculating average gain and average loss
    gain_ewm = gains.ewm(com=window - 1, adjust=False).mean()
    loss_ewm = abs(loss.ewm(com=window - 1, adjust=False).mean())

    RS = gain_ewm / loss_ewm
    getInfo["RSI"] = 100 - 100 / (1 + RS)

    return getInfo["RSI"]

def getBalanceSheet(ticker):
    tickInfo = yf.Ticker(ticker,session=session)
    financial_data = tickInfo.balance_sheet
    return financial_data

def getFinancial(ticker):
    tickInfo = yf.Ticker(ticker,session=session)
    financial_data = tickInfo.financials
    return financial_data

def IncomeDebtData(ticker):
    netIncomeData = getFinancial(ticker).loc['Net Income']
    netIncomeData = netIncomeData.reset_index()
    netIncomeData.columns = ['date','NetIncome']
    print(netIncomeData)
    latestDateNetIncome = netIncomeData.index.max()
    netIncome =  netIncomeData.loc[latestDateNetIncome,'NetIncome']
    
    print(getBalanceSheet(ticker))
    netDebtData = getBalanceSheet(ticker).loc['Net Debt']
    netDebtData = netDebtData.reset_index()
    netDebtData.columns = ['date','NetDebt']
    latestDateNetDebt = netDebtData.index.max()
    netDebt =  netDebtData.loc[latestDateNetDebt,'NetDebt']

    data = [(latestDateNetIncome,netIncome,latestDateNetDebt,netDebt)]

    return pd.DataFrame(data,columns=['Net_Income_Date','Net_Income','Net_Debt_Date','Net_Debt'])



