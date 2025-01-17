import pandas as pd
import matplotlib.pyplot as plt
import TimeSeries.GetData as gd
import numpy as np
from sklearn.preprocessing import StandardScaler

SMAValue=50
startDate='2023-01-01'
endDate='2024-11-01'
ticker='AAPL'

DateValue=gd.getSMA(ticker,SMAValue,startDate,endDate)[SMAValue-1:]
DateValue = DateValue.index

SMA=gd.getSMA(ticker,SMAValue,startDate,endDate)
RSI=gd.getRSI(ticker,startDate,endDate,14)
V=gd.getVolume(ticker,startDate,endDate)
ActualPrice=gd.getClosePrice(ticker,startDate,endDate)

#Initial Weights and bias value
Wsma=0.01
Wrsi=0.01
Wv=0.01
Wb=0.01

b=0.1
learningRate=0.1




#Cleaning
SMA = SMA.values[SMAValue-1:]

RSI = RSI.values[SMAValue-1:]

V = V.values.flatten()[SMAValue-1:]

ActualPrice = ActualPrice.values[SMAValue-1:]


# Initialize scaler
scaler = StandardScaler()


#Standardizing Features
features = np.column_stack((SMA, RSI, V))

# Fit and transform the data
scaled_features = scaler.fit_transform(features)

# Separate the scaled features
SMA = scaled_features[:, 0]
RSI = scaled_features[:, 1]
V = scaled_features[:, 2]

for i in range(100):
     PredictedPrice=SMA*Wsma+RSI*Wrsi+V*Wv+b
     ##Trying to calculate deravative here
     sum = 0
     for pp,ap,sm in zip(PredictedPrice,ActualPrice,SMA):
          sum = sum + (ap-pp) * sm
     drvWsma = (-2/len(PredictedPrice))*sum

     sum = 0
     for pp,ap,vol in zip(PredictedPrice,ActualPrice,V):
          sum = sum + (ap-pp) * vol
     drvWv = (-2/len(PredictedPrice))*sum

     sum = 0
     for pp,ap,rs in zip(PredictedPrice,ActualPrice,RSI):
          sum = sum + (ap-pp) * rs
     drvWrsi = (-2/len(PredictedPrice))*sum

     sum = 0
     for pp,ap in zip(PredictedPrice,ActualPrice):
          sum = sum + (ap-pp)
     drvB = (-2/len(PredictedPrice))*sum


     

     #Updating the weights

     Wsma=Wsma - learningRate * drvWsma
     Wrsi=Wrsi - learningRate * drvWrsi
     Wv=Wv - learningRate * drvWv
     b = b - learningRate * drvB


     MeanSquaredError = np.mean((ActualPrice - PredictedPrice) ** 2)
     print(f"Epoch {i+1}, Mean Squared Error: {MeanSquaredError}")

# MeanSquaredError = (ActualPrice - PredictedPrice)*(ActualPrice - PredictedPrice)

print(Wsma)

print(Wrsi)

print(Wv)

print(b)




######### Predicting Price ############


final_predicted_price = SMA * Wsma + RSI * Wrsi + V * Wv + b

# To evaluate the performance, calculate MSE for the final predictions
final_mse = np.mean((ActualPrice - final_predicted_price) ** 2)
print("Final Mean Squared Error:", final_mse)

# Optional: Plot Actual vs Predicted Price to visualize model performance
plt.figure(figsize=(12, 6))
plt.plot(DateValue,ActualPrice, label='Actual Price')
plt.plot(DateValue,final_predicted_price,label='Predicted Price', linestyle='--')
plt.title('Price Chart action '+ticker)
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.show()