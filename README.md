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