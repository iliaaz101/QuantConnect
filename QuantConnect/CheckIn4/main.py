#region imports
from AlgorithmImports import *
#endregion
class CheckIn4(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020,1,1) 
        self.SetEndDate(2021,1,1)
        self.SetCash(100000) #100k cash
        self.bp = self.AddEquity('BP',Resolution.Daily)
        self.xom = self.AddEquity('XOM', Resolution.Daily)
        self.invest_toggle = True
        self.sell_toggle = True

    def OnData(self,data):
        if not self.Portfolio.Invested and self.invest_toggle:
            self.SetHoldings(self.bp.Symbol, 0.5)
            self.SetHoldings(self.xom.Symbol, 0.5)
            self.invest_toggle = False

        if self.Portfolio.Invested and self.sell_toggle:
            bp_price = self.Portfolio[self.bp.Symbol].Price
            bp_shares = self.Portfolio[self.bp.Symbol].Quantity
            xom_price = self.Portfolio[self.xom.Symbol].Price 
            xom_shares = self.Portfolio[self.xom.Symbol].Quantity 
            self.StopMarketOrder(self.bp.Symbol, -bp_shares, bp_price*0.8) # meaning there's been a 20% reduction
            self.StopMarketOrder(self.xom.Symbol, -xom_shares, xom_price*0.8)
            self.sell_toggle = False
