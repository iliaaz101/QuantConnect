#region imports
from AlgorithmImports import *
#endregion
class BuyAndHold(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020,1,1)
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)
        self.AddEquity('XOM',Resolution.Daily)

    def OnData(self,data):
        if not self.Portfolio.Invested:
            self.SetHoldings('XOM',1)


            
