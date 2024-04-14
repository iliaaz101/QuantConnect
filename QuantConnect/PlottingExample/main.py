# region imports
from AlgorithmImports import *
# endregion

class PlottingExample(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        self.AddEquity("SPY", Resolution.Daily)
        
    def OnData(self, data):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        self.Plot("SPY Price", self.Securities['SPY'].Open)

