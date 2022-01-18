"""
Authors: Ryan Mulkey, Timothy Campbell, Robert Beery III

Description: This is a template for trading on a market (crypto currency, stocks, etc.).

Date Modified: 7/26/21
"""

class Trader:

    def __init__(self):
        self.balance = 0.00
        self.previousBuyPrice = 39000.0
        self.previousSellPrice = 0.0
        self.tradedItem = None

    def getBalance(self):
        return self.balance

    def setBalance(self, newBal):
        self.balance = newBal

    def getTradingItem(self):
        return self.tradedItem

    def setTradingItem(self, item):
        self.tradedItem = item

    def getPreviousSellPrice(self):
        return self.previousSellPrice

    def setPreviousSellPrice(self, newSellPrice):
        self.previousSellPrice = newSellPrice

    def getPreviousBuyPrice(self):
        return self.previousBuyPrice

    def setPreviousBuyPrice(self, newBuyPrice):
        self.previousBuyPrice = newBuyPrice

    def sell(self):
        return None

    def buy(self):
        return None