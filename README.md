# Complete Plan
## Collection of data
Stock History: This can be acquired using yfinance API. I can get historical information and various indicators from this website. Even, I can produce my own indicators.

News Data: I need to gather news about particular stock. Need to check what API I can use...

Fundamental Data: This includes earning and Quarterly reports. This information can be gathered using yfinance API as well.

## Choice of model
### Version 1
Start with Linear regression model and see how it works
The weights should be following:
a. RSI
b. Volume
c. SMA

Using gradient descent of MSE (Mean Squared Error) on provided weights, I will try to minimize the error between predicted and actual value.

![first Image](Maths/1.JPG)
![Second Image](Maths/2.JPG)
![Third Image](Maths/3.JPG)


#### Result of V1

![Fourth Image](Results/V1/V1_new.png)


#### Generating the future data
To generate the future data, we have to use time series analysis to analyze what effect would previous lags have on future data.
- Plot the PACF chart of each feature

Starting with Close Price first: 
The data is not stationary
![Fifth Image](Results/PACF/non_stationary_ClosePrice.png)

Using Differencing method for making the data stationary:
![Sixth Image](Results/PACF/stationarity_ClosePrice.png)

PACF CHART
![PACF Image](Results/PACF/PACF_of_ClosePrice.png)

ACF CHART
![ACF Image](Results/PACF/ACF_of_ClosePrice.png)

None of the lag shows any strong relationship between current and previous value.