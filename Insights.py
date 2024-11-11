import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

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

#Plotting the stationary data
#plt.plot(ActualPrice.index,ActualPrice['diff'],color='blue')

#Calculating PACF value
#pacf_values=sm.tsa.adfuller(ActualPrice['diff'])

#PACF PLOT
#plot_pacf(ActualPrice['diff'],ax=ax,lags=100)


#ACF PLOT
#plot_acf(ActualPrice['diff'],ax=ax,lags=100)
#plt.show()


#Calculate the right order
#stepwise_fit=auto_arima(ActualPrice['diff'],trace=True,suppress_warnings=True)

#stepwise_fit.summary()

# Best model:  ARIMA(2,0,2)(0,0,0)[0] intercept

#Create Training and Testing data set

training = ActualPrice['diff'].iloc[:-30]
testing = ActualPrice['diff'].iloc[-30:]

print(training)

print(testing)



p,d,q=2,0,2
# Fit an ARIMA model
model = ARIMA(training, order=(p,d,q))  # Replace (p,d,q) with appropriate values
model_fit = model.fit()

# Summary of the model
#print(model_fit.summary())


#Predicting values of testing set

start = len(training)
end = len(training) + len(testing) - 1
pred = model_fit.predict(start=start, end=end, type = 'levels')


#Reversing Difference
predicted_values = pred.cumsum() + ActualPrice[ticker][1:].iloc[:-30][-1]

Result = pd.DataFrame(data = ActualPrice[1:][-30:][ticker].values,index = DateValue.values[1:][-30:], columns=['Actual'])
Result['Predicted']=predicted_values.values
print(Result)

#The Result shows the price cannot be predicted only using Close Price as the feature

plt.plot(Result,label=['Actual','Predicted'])
plt.legend()
plt.show()