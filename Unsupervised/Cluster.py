import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")

import GetData as gd
import FinancialModellingPrep as sector



stockList = sector.fetchStocksUnderSegment("Technology")

print(stockList)