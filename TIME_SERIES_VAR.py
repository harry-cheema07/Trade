import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
from sklearn.preprocessing import StandardScaler
import Utils as util

SMAValue=50
startDate='2023-01-01'
endDate='2024-11-01'
ticker='AAPL'



SMA=gd.getSMA(ticker,SMAValue,startDate,endDate)
RSI=gd.getRSI(ticker,startDate,endDate,14)
Volume=gd.getVolume(ticker,startDate,endDate)
ActualPrice=gd.getClosePrice(ticker,startDate,endDate)


#Cleaning
SMA = SMA[SMAValue-1:]

RSI = RSI[SMAValue-1:]

Volume = Volume[SMAValue-1:]

ActualPrice = ActualPrice[SMAValue-1:]

DateValue = SMA.index
print(RSI)
#Making the data stationary
RSI['diff'] = util.stationary_differencing(RSI)

print(RSI)