import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
from sklearn.preprocessing import StandardScaler
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.tsa.api import VAR
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

#performing one more stationarity on SMA,Actual Price dataset
SMA['diff'] = util.stationary_differencing(SMA['diff'])
ActualPrice['diff'] = util.stationary_differencing(ActualPrice['diff'])



#Plotting the data to verify stationarity
#util.plotStationarity(ActualPrice)


#Testing Stationarity with Augmented Dickey-Fuller test
print(sm.tsa.adfuller(ActualPrice['diff']))


#Plotting PACF plot to calculate lags
#plot_pacf(ActualPrice['diff'])
#plt.show()


# Initialize scaler
scaler = StandardScaler()


#Standardizing Features
features = np.column_stack((SMA['diff'], RSI['diff'], Volume['diff'],ActualPrice['diff']))

# Fit and transform the data
scaled_features = scaler.fit_transform(features)

# Separate the scaled features
SMA['diff'] = scaled_features[:, 0]
RSI['diff'] = scaled_features[:, 1]
Volume['diff'] = scaled_features[:, 2]
ActualPrice['diff'] = scaled_features[:, 3]



#Creating a single data frame with all features in it






training_data=pd.DataFrame()
training_data['volumeDiff'] = Volume['diff']
training_data['SMADiff'] = SMA['diff']
training_data['RSIDiff'] = RSI['diff']
training_data['APDiff'] = ActualPrice['diff']
print(training_data)




model = VAR(training_data)
model_fit = model.fit(maxlags=5)
print(model_fit.summary())


#Reversing Scaler for 1stNov
z = -0.92863  # Scaled prediction
mu = scaler.mean_[3]  # Replace column_index with the correct index
sigma = scaler.scale_[3]

# Calculate original value
original_price = z * sigma + mu
print("Original Predicted Price:", original_price)


#Reversing Differencing for 1stNov
ActualValue=-3.2988610461665977+225.91
print(ActualValue)