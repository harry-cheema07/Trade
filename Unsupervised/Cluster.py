import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

import pandas as pd
import GetData as gd
import FinancialModellingPrep as sector

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

stocksInSegments = {}

segments = sector.fetchAllSegments()


#for now I am reducing the number of sectors for API's daily limit
#segments = segments[:2]


#Loading the stocks in their respective segments
for i in segments:
    stocksInSegments[i] = sector.fetchStocksUnderSegment(i)





#Getting financial data for all stocks and storing that in a df

#flattening the file 
flattened_data = []

for segment,tickers in stocksInSegments.items():
    for ticker in tickers:
        if sector.fetchFinancial(ticker) != None:
            flattened_data.append((segment,ticker,sector.fetchFinancial(ticker)[0]['date'],sector.fetchFinancial(ticker)[0]['eps'],sector.fetchFinancial(ticker)[0]['netIncome']  ))
df=pd.DataFrame(flattened_data,columns=["Segment","Ticker","date","EPS","NetIncome"])

print(df)


# Standardize the data (important for clustering)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)


kmeans = KMeans(n_clusters=8, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)


plt.figure(figsize=(8, 6)) 
plt.scatter(scaled_features['EPS'], scaled_features['NetIncome'], hue=scaled_features['Cluster'],
    palette='viridis',
    s=100) 
plt.title('K-Means Clustering') 
plt.xlabel('Scaled EPS') 
plt.ylabel('Scaled Net Income') 
plt.grid(True) 
plt.show()