# region imports
from AlgorithmImports import *
from System.Drawing import Color
# endregion

class ModifyingPlot(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 1)
        self.SetCash(100000)
        self.AddEquity("SPY", Resolution.Daily)

        price_plot = Chart('Custom Chart')
        price_plot.AddSeries(Series('Price',SeriesType.Line,'%',Color.Green,0))
        self.AddChart(price_plot)

    def OnData(self, data: Slice):
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)

        self.Plot("Custom Chart", "Price", self.Securities['SPY'].Open)
