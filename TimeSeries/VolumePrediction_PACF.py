import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")


import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from sklearn.metrics import mean_squared_error
from math import sqrt

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

RSI = RSI[SMAValue-1:]

V = V[SMAValue-1:]

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



##Checking the stationarity of the Volume

pacf_values=sm.tsa.adfuller(V)


print(pacf_values)


#stepwise_fit=auto_arima(V,trace=True,suppress_warnings=True)

stepwise_fit=auto_arima(   V,  # Replace `V` with your Volume data variable
    seasonal=True,
    m=5,
    trace=True,
    suppress_warnings=True,
    stepwise=True,
    error_action='ignore',
    max_p=3, max_q=3, max_d=1,
    max_P=3, max_Q=3, max_D=1  # Seasonal parameters for SARIMA)
)
stepwise_fit.summary()





training = V.iloc[:-30]
testing = V.iloc[-30:]



p,d,q=4,0,2
# Fit an ARIMA model
model = ARIMA(training, order=(p,d,q))  # Replace (p,d,q) with appropriate values
model_fit = model.fit()

# Summary of the model
#print(model_fit.summary())


#Predicting values of testing set

start = len(training)
end = len(training) + len(testing) - 1
pred = model_fit.predict(start=start, end=end, type = 'levels')

Result = pd.DataFrame(data = V[1:][-30:][ticker].values,index = DateValue.values[1:][-30:], columns=['Actual'])
Result['Predicted']=pred.values
print(Result)

rmse = sqrt(mean_squared_error(Result['Predicted'],Result['Actual']))
#The Result shows the price cannot be predicted only using Close Price as the feature
print(rmse)
plt.plot(Result,label=['Actual','Predicted'])
plt.legend()
plt.show()