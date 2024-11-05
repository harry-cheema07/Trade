import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np

SMAValue=50
startDate='2023-01-01'
endDate='2024-11-01'
ticker='AAPL'
learningRate=0.01

SMA=gd.getSMA(ticker,SMAValue,startDate,endDate)
RSI=gd.getRSI(ticker,startDate,endDate,14)
V=gd.getVolume(ticker,startDate,endDate)

#Initial Weights and bias value
Wsma=1
Wrsi=2
Wv=3
b=4



ActualPrice=gd.getClosePrice(ticker,startDate,endDate)

#Setting first few values as null because Moving averages will be null for first few records
ActualPrice[:SMAValue-1]=np.nan
ActualPrice = ActualPrice[~np.isnan(ActualPrice).any(axis=1)]

#Cleaning the Arrays from null values



#print(PredictedPrice)
#print(ActualPrice.values.flatten())
#print(MeanSquaredError)

for i in range(10):
     PredictedPrice=SMA.values*Wsma+RSI.values*Wrsi+V.values.flatten()*Wv+b
     PredictedPrice = PredictedPrice[~np.isnan(PredictedPrice)]
     ##Trying to calculate deravative here
     sum = 0
     for pp,ap,sm in zip(PredictedPrice,ActualPrice.values.flatten(),SMA.values[SMAValue-1:]):
          sum = sum + (ap-pp) * sum
     drvWsma = (-2/len(PredictedPrice))*sum

     sum = 0
     for pp,ap,vol in zip(PredictedPrice,ActualPrice.values.flatten(),V.values.flatten()[SMAValue-1:]):
          sum = sum + (ap-pp) * vol
     drvWv = (-2/len(PredictedPrice))*sum

     sum = 0
     for pp,ap,rs in zip(PredictedPrice,ActualPrice.values.flatten(),RSI.values[SMAValue-1:]):
          sum = sum + (ap-pp) * rs

     drvWrsi = (-2/len(PredictedPrice))*sum

     #Updating the weights

     Wsma=Wsma - learningRate * drvWsma
     Wrsi=Wrsi - learningRate * drvWrsi
     Wv=Wv - learningRate * drvWv




MeanSquaredError = (ActualPrice.values.flatten() - PredictedPrice)*(ActualPrice.values.flatten() - PredictedPrice)

print(MeanSquaredError)