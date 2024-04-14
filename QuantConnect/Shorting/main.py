# region imports
from AlgorithmImports import *
# endregion

class Shorting(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        self.seaworld = self.AddEquity("SEAS", Resolution.Daily)
        self.invest = True

    def OnData(self, data):
        if not self.Portfolio.Invested and self.invest:
            # Because we don't already own the share, we're actually shorting the position
            # SHORT == SELL WITHOUT OWNING/PURCHASING FIRST
            self.SetHoldings(self.seaworld.Symbol, -1)

        if self.Time.month == 5:
            self.Liquidate(self.seaworld.Symbol)
            self.invest = False
