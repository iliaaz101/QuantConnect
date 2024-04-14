# region imports
from AlgorithmImports import *
# endregion

class UpdateOrderTicket(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2007,1,1)  # Set Start Date
        self.SetEndDate(2010,1,1)
        self.SetCash(100000)  # Set Strategy Cash
        self.citi = self.AddEquity("C", Resolution.Daily)
        self.citi.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.c = self.citi.Symbol
        self.first_day_close = None
        self.sellTicket = None
        self.invest = True
        self.loss_limit = 0.5

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested and self.invest:
            self.initial_order = self.MarketOrder(self.c,10)
            self.first_day_close = self.Securities['C'].Close
            self.invest = False
        
        if self.sellTicket is None:
            # if the price ever drops 50% below the first day closing price, initiate a StopMarketOrder
            self.sellTicket = self.StopMarketOrder(self.c, -10,
            self.Securities['C'].Close*self.loss_limit, "Stop Loss")

    def OnEndOfDay(self):
        if self.sellTicket is None:
            return 
        
        else:
            # start logging the closing price when the StopMarketOrder is made
            self.Log(str(self.Securities['C'].Close))

        # Checking for 5% drop everyday from Open --> Close
        # Update the Stop Price: 50% stop loss --> 75% stop loss
        price_diff_perc = (self.Securities['C'].Open - self.Securities['C'].Close)/self.Securities['C'].Open

        if price_diff_perc > 0.05:
            updateSettings = UpdateOrderFields()
            updateSettings.StopPrice = self.first_day_close * 0.75

            response = self.sellTicket.Update(updateSettings)

            if response.IsSuccess:
                self.Debug("Order was Updated!")

    def OnOrderEvent(self, OrderEvent):
        if OrderEvent.FillQuantity == 0:
            return

        fetched = self.Transactions.GetOrderById(OrderEvent.OrderId)
        self.Log(f"{str(fetched.Type)} filled, for {str(OrderEvent.FillQuantity)}")
