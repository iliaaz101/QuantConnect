#region imports
from AlgorithmImports import *
#endregion
class SellAtPrice(QCAlgorithm):

    def Initialize(self):

        self.SetCash(10000)
        self.SetStartDate(2010,1,1)
        self.SetEndDate(2020,1,1)

        self.apple = self.AddEquity('AAPL',Resolution.Daily)

        self.limit_price = 50
        self.invest = True

    def OnData(self,data):

        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings('AAPL',1)

        closing_price = self.Portfolio['AAPL'].Price


        if closing_price > self.limit_price and self.Portfolio.Invested:
            self.Liquidate('AAPL')
            self.invest = False
