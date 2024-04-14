#region imports
from AlgorithmImports import *
#endregion
class SellOrder(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2008,1,1)
        # no self.SetEndDate --> ongoing/to present
        self.SetCash(100000)
        self.stock = self.AddEquity('IBM',Resolution.Daily)
        self.invest = True

    def OnData(self,data):
        if not self.Portfolio.Invested and self.invest:
            # setting a limit order
            # Buy 10 shares of IBM -- MAX price willing to pay $50
            # .limitOrder(stock symbol, # of shares, limit price)
            self.LimitOrder(self.stock.Symbol,10,50)

            # SELL 10 shares -- MIN price willing to sell is $100
            self.LimitOrder(self.stock.Symbol,-10,100)

            self.invest = False
