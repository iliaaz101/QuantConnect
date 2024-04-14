# region imports
from AlgorithmImports import *
# endregion

class StopMarketOrder(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019,1,1)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        # Ticker for Boeing Company
        self.ba = self.AddEquity('BA', Resolution.Daily)
        self.invest = True

        # The ticket identifier of our order
        self.sell_ticket = None

    # OnData is running on a loop
    def OnData(self,data):
        if not self.Portfolio.Invested and self.invest:
            # First Day Close Price
            self.MarketOrder(self.ba.Symbol,10)
            self.invest = False
        
        # code below runs once on the first day
        if self.sell_ticket == None:
            # STOP PRICE TRIGGER = 60% on initial Open Price
            self.sell_ticket = self.StopMarketOrder(self.ba.Symbol, -10, self.Securities['BA'].Open*0.6,'Sell BA')
