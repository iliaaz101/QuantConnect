#region imports
from AlgorithmImports import *
#endregion
class CheckIn2(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,1,1)
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)
        self.AddEquity("KO",Resolution.Daily)
        self.invest = True

    def OnData(self,data):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("KO",0.5)
            self.invested_time = self.Time
        
        self.Log(self.Time - self.invested_time)
        time_diff = (self.Time - self.invested_time).days
        if time_diff > 100:
            self.Liquidate("KO")
            self.invest = False

