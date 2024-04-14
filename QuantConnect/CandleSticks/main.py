# region imports
from AlgorithmImports import *
# endregion

class CandleStick(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 1, 2)
        self.SetCash(100000)
        self.AddEquity("SPY", Resolution.Daily)

        price_plot = Chart("Candle Plot")
        price_plot.AddSeries(Series("Price",SeriesType.Candle,0))
        self.AddChart(price_plot)

    # this function runs everyday
    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        # adds a plot each to the custom chart each day that's its running
        self.Plot("Candle Plot", "Price", self.Securities['SPY'].Price)
