import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
from sklearn.preprocessing import StandardScaler
import Utils as util
import datetime
import statsmodels.api as sm

SMAValue=50
startDate='2023-01-01'
endDate='2024-11-01'
ticker='AAPL'



SMA=gd.getSMA(ticker,SMAValue,startDate,endDate)
RSI=gd.getRSI(ticker,startDate,endDate,14)
Volume=gd.getVolume(ticker,startDate,endDate)
ActualPrice=gd.getClosePrice(ticker,startDate,endDate)


#Cleaning
SMA = SMA[SMAValue-1:].to_frame()

RSI = RSI[SMAValue-1:]

Volume = Volume[SMAValue-1:]

ActualPrice = ActualPrice[SMAValue-1:]

DateValue = SMA.index

#Making the data stationary
RSI['diff'] = util.stationary_differencing(RSI)

SMA['diff'] = util.stationary_differencing(SMA)

Volume['diff'] = util.stationary_differencing(Volume)

ActualPrice['diff'] = util.stationary_differencing(ActualPrice)

#performing one more stationarity on SMA dataset
SMA['diff'] = util.stationary_differencing(SMA['diff'])


#Plotting the data to verify stationarity
util.plotStationarity(RSI)


#Testing Stationarity with Augmented Dickey-Fuller test
print(sm.tsa.adfuller(RSI['diff']))