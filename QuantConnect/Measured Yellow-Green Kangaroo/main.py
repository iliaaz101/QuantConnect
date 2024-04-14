# region imports
from AlgorithmImports import *
# endregion

class MeasuredYellowGreenKangaroo(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 9, 3)
        self.SetCash(100000)
        self.AddEquity("SPY", Resolution.Daily)

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)
