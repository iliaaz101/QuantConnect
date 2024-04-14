# region imports
from AlgorithmImports import *
# endregion

class StopLimitOrder(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,1,1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily)

    def OnData(self, data):
        if not self.Portfolio.Invested:
            
            # First Day Closing Price
            close = self.Securities['SPY'].Close
            # 1% drop --> Stop Triggered
            stop_price = close *0.99
            # Limit 1% above close price
            limit_price = close * 1.01

            self.StopLimitOrder(self.spy.Symbol,10,stop_price,limit_price)
