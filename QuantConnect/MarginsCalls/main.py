# region imports
from AlgorithmImports import *
# endregion

class MarginCalls(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021,1,1)
        self.SetCash(100000)
        self.spy = self.AddEquity("SPY", Resolution.Daily)
        self.Securities['SPY'].SetLeverage(100)
        self.invest = True

    def OnData(self, data):
        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("SPY", 99)
            self.invest = False
    
    # def OnMarginCallWarning(self):
    #     self.Log(f"MARGIN: {self.Portfolio.MarginRemaining}")
    #     self.Liquidate(self.spy.Symbol) 

    def OnMarginCall(self,requests):

        #When I get a margin call, grab the order and sell 10% than what the broker wants
        for order in requests:
            new_quantity = int(order.Quantity*1.1)
            requests.remove(order)
            new_order = SubmitOrderRequest(order.OrderType, order.securityType, order.Symbol, new_quantity, order.StopPrice, order.LimitPrice, self.Time, 'OnMarginCall')
            requests.append(new_order)
        return requests
