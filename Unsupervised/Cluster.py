import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

import GetData as gd
import FinancialModellingPrep as sector


stocksInSegments = {}

segments = sector.fetchAllSegments()
segments = segments[:2]

#for now I am reducing the number of sectors for API's daily limit

#Loading the stocks in their respective segments
for i in segments:
    stocksInSegments[i] = sector.fetchStocksUnderSegment(i)

#Getting financial data for all stocks and storing that in a df
print(stocksInSegments)