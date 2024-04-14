from datetime import datetime
#region imports
from AlgorithmImports import *
#endregion
class MarketOrder(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010,1,1)
        self.SetEndDate(2015,1,1)
        self.SetCash(1000000)
        self.stock = self.AddEquity('SPY',Resolution.Daily)
        self.invest = True

    def OnData(self,data):
        if not self.Portfolio.Invested and self.invest:
            # making a market order of buying 1000 shares
            # 1000 (positive) means to buy 1000 shares
            self.MarketOrder(self.stock.Symbol,1000) 
            self.invest = False 

        if self.Time == datetime(day=1,month=1,year=2014):
            # making a market order of selling 1000 shares
            # -1000 (negative) means to sell 1000 shares
            self.MarketOrder(self.stock.Symbol,-1000)
