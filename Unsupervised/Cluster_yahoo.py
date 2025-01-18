import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

import plotly.express as px
import pandas as pd
import GetData as gd
import FinancialModellingPrep as sector

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]


stockData = sp500[['Symbol','GICS Sector']].rename(columns={'Symbol':'Ticker','GICS Sector':'Sector'})
stockData = stockData.head(100)
for Index,Row in stockData.iterrows():
    if gd.getPercentageChange(Row.Ticker) != None:
        change=gd.getPercentageChange(Row.Ticker)
        volume=gd.getPreviousVolume(Row.Ticker)
        stockData.at[Index, 'Change'] = change
        stockData.at[Index, 'Volume'] = volume
        

#Standardizing numbers

# Separate numerical and categorical columns 
# numerical_cols = stockData.select_dtypes(include=['number']).columns 
# categorical_cols = stockData.select_dtypes(include=['object']).columns


# scaler = StandardScaler()
# stockData[numerical_cols] = scaler.fit_transform(stockData[numerical_cols])

# # Combine the standardized numerical data with the original categorical data 
# scaled_stock_data = pd.concat([stockData[categorical_cols], stockData[numerical_cols]], axis=1)


# print(scaled_stock_data)

#Segment Growth Calculation
segment_growth = stockData.groupby('Sector')['Change'].mean().reset_index().sort_values(by='Change', ascending=False)

print(segment_growth)

#Plotting

fig = px.scatter(stockData, x='Volume', y='Change', text='Ticker',color='Sector', title='Stock/Segment Price Action')
fig.update_traces(marker=dict(size=12), selector=dict(mode='markers+text'))
fig.show()