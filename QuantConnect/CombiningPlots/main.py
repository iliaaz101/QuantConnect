# region imports
from AlgorithmImports import *
# endregion

class CombiningPlots(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021,1,1)
        self.SetCash(100000)

        self.AddEquity("SPY", Resolution.Daily)

        price_plot = Chart("My Plot")
        price_plot.AddSeries(Series('Price',SeriesType.Line,0))
        price_plot.AddSeries(Series('Monthly Open Price',SeriesType.Scatter,1))
        self.AddChart(price_plot)

    def OnData(self, data):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        self.Plot('My Plot','Price',self.Securities['SPY'].Open)

        # at the beginning of each month
        if self.Time.day == 1:
            self.Plot('My Plot', 'Monthly Open Price',self.Securities['SPY'].Open)


        
