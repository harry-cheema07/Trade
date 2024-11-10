import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.tsa.arima.model import ARIMA

SMAValue=50
startDate='2023-01-01'
endDate='2024-11-01'
ticker='AAPL'



SMA=gd.getSMA(ticker,SMAValue,startDate,endDate)
RSI=gd.getRSI(ticker,startDate,endDate,14)
V=gd.getVolume(ticker,startDate,endDate)
ActualPrice=gd.getClosePrice(ticker,startDate,endDate)


#Cleaning
SMA = SMA[SMAValue-1:]

RSI = RSI.values[SMAValue-1:]

V = V.values.flatten()[SMAValue-1:]

ActualPrice = ActualPrice[SMAValue-1:]

DateValue=gd.getSMA(ticker,SMAValue,startDate,endDate)[SMAValue-1:]
DateValue = DateValue.index

### PACF on SMA


# N = 206

# # Calculate the confidence interval bounds
# conf_interval = 1.96 / np.sqrt(N)



# pacf_values = sm.tsa.pacf(SMA, nlags=206)
# print(pacf_values)

# #Plotting PACF chart
# plt.stem(range(len(pacf_values)),pacf_values)
# #plt.bar(range(len(pacf_values)),pacf_values, width=0.4)
# plt.xlabel('Lags')
# plt.ylabel('PACF')
# plt.title('Partial Autocorrelation Function')

# #Plotting confidence lines

# plt.axhline(y=conf_interval, color='red', linestyle='--', linewidth=1)
# plt.axhline(y=-conf_interval, color='red', linestyle='--', linewidth=1)


# plt.show()




#PACF in Close Price

fig, ax =plt.subplots(figsize=(10, 6))
##Checking the stationarity of the Close Price
#plt.plot(ActualPrice,color='blue')


#Using Differencing method making the data stationary
first_diffs = ActualPrice.values[1:] - ActualPrice.values[:-1]
first_diffs = np.concatenate([first_diffs.flatten(), [0]])
ActualPrice['diff'] = first_diffs
print(len(ActualPrice.index))
print(len(ActualPrice['diff']))
#Plotting the stationary data
#plt.plot(ActualPrice.index,ActualPrice['diff'],color='blue')
print(ActualPrice['diff'])
#Calculating PACF value
pacf_values=sm.tsa.adfuller(ActualPrice['diff'])
print(pacf_values)
#PACF PLOT
#plot_pacf(ActualPrice['diff'],ax=ax,lags=100)


#ACF PLOT
plot_acf(ActualPrice['diff'],ax=ax,lags=100)
plt.show()


# p,d,q=0,0,0
# # Fit an ARIMA model
# model = ARIMA(ActualPrice['diff'], order=(p,d,q))  # Replace (p,d,q) with appropriate values
# model_fit = model.fit()

# # Summary of the model
# print(model_fit.summary())
