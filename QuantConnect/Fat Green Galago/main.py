# region imports
from AlgorithmImports import *
# endregion

class Leverage(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021, 1, 1)
        self.SetCash(10000)
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Cash)
        self.spy = self.AddEquity("SPY", Resolution.Daily)

        self.spy.SetLeverage(2)

    def OnData(self, data):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 2)

