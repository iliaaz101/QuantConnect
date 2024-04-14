# region imports
from AlgorithmImports import *
# endregion

class ConditionalPurchasing(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2020,1,1) 
        self.SetCash(100000)

        self.vnq = self.AddEquity("VNQ", Resolution.Daily)
        self.vnqi = self.AddEquity("VNQI", Resolution.Daily)

    def OnData(self, data):
        
        # DAILY GAIN (2%)
        vnqi_gain = (self.vnqi.Close - self.vnqi.Open)/self.vnqi.Open
        vnq_gain = (self.vnq.Close - self.vnq.Open)/self.vnq.Open

        # VNQI gain >2% and VNQI gain > VNQ gain --> 100% Holdings into VNQ
        if vnqi_gain > 0.02 and vnqi_gain > vnq_gain:
            self.SetHoldings(self.vnq.Symbol,1,True)
            self.Log(f"VNQI Gain: {vnqi_gain}")

        # VNQ > 2% and VnQ gain > VQNI --> 100% holdings into VNQI
        if vnq_gain > 0.02 and vnq_gain > vnqi_gain:
            self.SetHoldings(self.vnqi.Symbol, 1, True)
            self.Log(f"VNQ Gain: {vnq_gain}")

        else:
            self.Log('No action taken')
            return
