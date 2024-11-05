import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
ticker='AAPL'
data=gd.getData(ticker)

volume=data['Volume']

print(data)