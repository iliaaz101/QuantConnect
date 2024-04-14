# region imports
from AlgorithmImports import *
# endregion

class UniverseSelection(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021,2,1)
        self.SetCash(100000000)

        # SET UP THE UNIVERSE
        # 1) Set the resolution of the universe
        self.UniverseSettings.Resolution = Resolution.Daily
        #everyday, the above code will run because of our resolution
        self.AddUniverse(self.CoarseSelection,self.FineSelection)
   
    def CoarseSelection(self,coarse):

        self.filtered_by_price = [sec.Symbol for sec in coarse if sec.Price> 20 and sec.DollarVolume > 1000000 and sec.HasFundamentalData]

        return self.filtered_by_price
    
    def FineSelection(self, fine):
        self.filtered_by_pe = [sec for sec in fine if sec.ValuationRatios.PERatio < 100]

        sorted_by_ebit = sorted(self.filtered_by_pe,key=lambda x:x.FinancialStatements.IncomeStatement.EBIT.TwelveMonths,reverse = True)

        self.list_of_symbols = [x.Symbol for x in sorted_by_ebit]
        
        return self.list_of_symbols

    def OnData(self, data: Slice):
        # if not self.Portfolio.Invested:
        #     # self.SetHoldings("SPY", 1)

        self.Log(self.Time)

        for sec in self.Securities.Values:
            
            if not data.ContainsKey(sec.Symbol) or not data[sec.Symbol]:
                return
            
            self.Log(f"{data[sec.Symbol].Symbol} opened at : {data[sec.Symbol].Open}")
        
        self.Log("------DAY OVER-------")
    
    def OnSecuritiesChanged(self, changes):
        self.Log("CHANGE IN UNIVERSE")

        for sec in changes.RemovedSecurities:
            self.Liquidate(sec.Symbol)
            self.Log(f"SOLD: {sec}")

        for sec in changes.AddedSecurities:
            self.SetHoldings(sec.Symbol,0.1)
            self.Log(f"BOUGHT: {sec}")


