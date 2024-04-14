from datetime import datetime
# region imports
from AlgorithmImports import *
# endregion

class MarketOnOrders(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,1,1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily)
        self.invest = True

    def OnData(self, data):
        if not self.Portfolio.Invested and self.invest:
            self.MarketOnOpenOrder(self.spy.Symbol,10)
            self.invest = False

        if self.Time > datetime(2020,1,30):
            self.MarketOnCloseOrder(self.spy.Symbol, 10)

"""THERE'S SOMETHING WRONG WITH THIS FILE, LIMIT ORDER KEEPS REPEATING (8- PGS OF ORDERS)"""
