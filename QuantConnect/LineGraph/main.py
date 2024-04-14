# region imports
from AlgorithmImports import *
# endregion

class LineGraph(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 9, 3)
        self.SetCash(100000)
        self.AddEquity("SPY", Resolution.Daily)

        # 1) CREATE A CHART OBJECT
        price_plot = Chart("Custom Chart")

        #2) GRAPH THE CHART AND ADD SERIES/PLOT TYPE
        # Lots of customization happens at AddSeries
        price_plot.AddSeries(Series('Price',SeriesType.Line,0))

        #3) ADD THE CHART TO THE BACKTEST
        self.AddChart(price_plot)

    # this function runs everyday
    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        # adds a plot each to the custom chart each day that's its running
        self.Plot("Custom Chart", "Price",self.Securities['SPY'].Open)
