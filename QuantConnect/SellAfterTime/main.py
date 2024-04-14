#region imports
from AlgorithmImports import *
#endregion
class SellAfterTime(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015,1,1) #set start Date
        self.SetEndDate(2021,1,1)
        self.SetCash(10000) # Set strategy cash
        self.AddEquity("SPY",Resolution.Daily)
        self.invest = True

    def OnData(self,data):

        """
        if we havent invested in our portfolio
        AND self.invest is true
        """
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("SPY",1)
            self.invested_time = self.Time #DATETIME object

        # LIQUIDATE AFTER 1000 DAYS
        # checks the day everytime using self.Time
        self.Log(self.Time - self.invested_time)
        time_diff = (self.Time - self.invested_time).days

        if time_diff > 1000:
            self.Liquidate('SPY')
            self.invest = False

