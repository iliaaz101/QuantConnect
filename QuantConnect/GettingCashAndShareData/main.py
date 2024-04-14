# region imports
from AlgorithmImports import *
# endregion

class GettingCashAndShareData(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015,1,1)  # Set Start Date
        self.SetEndDate(2020,1,1)
        self.SetCash(100000)  # Set Strategy Cash
        self.apple = self.AddEquity("AAPL", Resolution.Daily)

        self.invest_toggle = True
        self.sell_toggle = True

    def OnData(self, data: Slice):
        if not data[self.apple.Symbol]:
            return #returns if we have no apple shares, just return
        
        if not self.Portfolio.Invested and self.invest_toggle:

            # Divide the cash we have by the opening price of apple
            # We get how many total shares we can buy
            shares_to_buy = int(self.Portfolio.Cash / data[self.apple.Symbol].Open)
            self.MarketOrder(self.apple.Symbol,shares_to_buy)

            self.invest_toggle = False
            return
        
        profit = self.Portfolio[self.apple.Symbol].UnrealizedProfitPercent

        # if 10% profit reached, then sell half of our shares
        if profit >= 0.1 and self.sell_toggle:

            held_shares = self.Portfolio[self.apple.Symbol].Quantity

            self.MarketOrder(self.apple.Symbol, int(-(held_shares/2)))
            self.sell_toggle = False
            return
        
    def OnOrderEvent(self, orderEvent):
        # if we execute an order, we get an order event
        # once we make an order, an order ticket is produced, which initiates an orderEvent
    
        if orderEvent.FillQuantity == 0:
            return
        
        fetched = self.Transactions.GetOrderById(orderEvent.OrderId)

        self.Log(f"{str(fetched.Type)} was filled")
        self.Log(f"Symbol was: {str(orderEvent.Symbol)}")
        self.Log(f"Quantity was: {str(orderEvent.FillQuantity)}")
