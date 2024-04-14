# region imports
from AlgorithmImports import *
# endregion

class SchedulingFunctions(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019,1,1)  # Set Start Date
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)  # Set Strategy Cash
        self.tesla = self.AddEquity('TSLA', Resolution.Daily)

        # At the start of every month, trigger the Buy method at 09:30 (24hr clock)
        self.Schedule.On(self.DateRules.MonthStart(),
                        self.TimeRules.At(9,30),
                        self.Buy)

        self.monthly_buy = 200
        self.cash_reserve = 200
        """Every month, I can spend $200 to buy tesla stocks.
        If I can't buy a tesla stock with 200, then I add that 200 amount to my cash reserve.
        If I can"""

    def Buy(self):

        # TSLA stock once a month

        # Cash vs. TSLA Price Open
        if self.Portfolio.Cash < self.tesla.Open:
            self.Debug("Not Enough Cash!")
            return


        # LIMIT $200/month
        # limit vs. TSLA price
        # cash_reserve + $200 DCA
        elif self.tesla.Open > self.cash_reserve:
            self.cash_reserve += self.monthly_buy
            self.Log("Stock too expensive!")
            return
        
        shares_to_buy = int(self.cash_reserve/self.tesla.Open)
        self.Log(f"Buying Shares: {shares_to_buy}")
        self.MarketOrder(self.tesla.Symbol, shares_to_buy)
        self.cash_reserve = self.monthly_buy
