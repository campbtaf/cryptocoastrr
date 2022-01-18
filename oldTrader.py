from Trader import Trader


class OldTrader(Trader):
    def __init__(self, initdata):
        Trader.__init__(self, initdata)

    # def getBalance(self):
    #     return self.balance
    #
    # def setBalance(self, newBal):
    #     self.balance = newBal

    # def getTradingItem(self):
    #     return 'BTC-USD'
    #
    # def setTradingItem(self, item):
    #     self.tradedItem = item

    # def getPreviousSellPrice(self):
    #     return self.previousSellPrice
    #
    # def setPreviousSellPrice(self, newSellPrice):
    #     self.previousSellPrice = newSellPrice
    #
    # def getPreviousBuyPrice(self):
    #     return self.previousBuyPrice
    #
    # def setPreviousBuyPrice(self, newBuyPrice):
    #     self.previousBuyPrice = newBuyPrice

    def sell(self):
        newBalance = (self.balance * (self.getPreviousSellPrice() / self.getPreviousBuyPrice()))
        self.setBalance(newBalance)
        print("I sold bitcoin for ", self.getPreviousSellPrice(), " and now have ", self.balance)
              #, "now waiting for transaction time.")
        #time.sleep(600)


    def buy(self):
        print("I bought bitcoin for ", self.getPreviousBuyPrice(), " with ", self.balance)
              #, "now waiting for transaction time.")
        #time.sleep(600)