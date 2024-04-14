#region imports
from AlgorithmImports import *
#endregion
class CheckIn3(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015,1,1)
        self.SetEndDate(2020,1,1)
        self.SetCash(10000)
        self.AddEquity("BRK.B",Resolution.Daily)
        self.invest = True
        self.limit_profit_percent = 0.2

    def OnData(self,data):

        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("BRK.B",1)
        
        profit_percent = self.Portfolio['BRK.B'].UnrealizedProfitPercent

        if profit_percent >= self.limit_profit_percent:
            self.Liquidate("BRK.B")
            self.invest = False


