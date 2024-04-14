#region imports
from AlgorithmImports import *
#endregion
"""
1) Selling after a profit has been made
2) Selling after a percentage of loss has occurred

UnrealizedProfitPercent Attribute:
This is a value ranging from -1 to N
 -1 indicates 100% loss (firm lower limnit)

 N indicates N*100 profit gain (technically no higher limit)
"""

class SellOnProfit(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2018,1,1)
        self.SetEndDate(2021,1,1)
        self.SetCash(10000)
        self.AddEquity("AAL",Resolution.Daily)

        self.invest = True

        # 100% profit --> SELL (lock-in profits)
        # self.limit_profit_percent = 0.5

        # 50% LOSS --> SELL
        self.limit_profit_percent = -0.5

    def OnData(self,data):

        if not self.Portfolio.Invested and self.invest:
            self.SetHoldings("AAL",1)
        
        profit_percent = self.Portfolio['AAL'].UnrealizedProfitPercent

        # if profit_percent > self.limit_profit_percent:
        #     self.Liquidate("AAL")
        #     self.invest = False
        
        if profit_percent < self.limit_profit_percent:
            self.Liquidate('AAL')
            self.invest = False

