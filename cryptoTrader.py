"""
Authors: Ryan Mulkey, Timothy Campbell, Robert Beery III

Description: This is a crypto currency trader based on the Trader.py interface. It uses the Coinbase API to trade on
             the market, and calculates in any fees for the price at time of buy to allow for a positive sell.

Date Modified: 7/27/21
"""

from Trader import Trader
import json, requests, time
from cbAuthenticate import CoinbaseWalletAuth
from messageTexter import messageTexter

class cryptoTrader(Trader):
    def __init__(self):
        Trader.__init__(self)

        jsonFin = open('config.json', 'r')
        jsonData = json.load(jsonFin)
        jsonFin.close()

        self.api_url = jsonData.get("api_url")
        self.auth = CoinbaseWalletAuth(jsonData.get("api_key"), jsonData.get("secret"), jsonData.get("passphrase"))
        self.tradedItem = jsonData.get("coin")

    def sell(self):
        currentMoney = self.getUSDBalance()
        currentCoin = self.getCoinBalance()

        sellInfo = {
            "size": str(currentCoin),
            "side": "sell",
            "product_id": str(self.tradedItem)+"-USD",
            "type": "market"
        }
        sellInfo = json.dumps(sellInfo)
        sellRequest = requests.post(self.api_url + 'orders', auth=self.auth, data=sellInfo)

        messageTexter("Attempting to sell. Waiting for transaction to complete.")
        while True:
            if self.getUSDBalance() > currentMoney or currentCoin < self.getCoinBalance():
                break
            time.sleep(30)

        messageTexter("I sold " + str(self.tradedItem) + " for " + str(self.getPreviousSellPrice()) + " and now have " + str(self.getUSDBalance()) + '.')


    def buy(self):
        currentMoney = self.getUSDBalance()
        currentCoin = self.getCoinBalance()
        buyInfo = {
            "size": round(currentMoney, 8),
            "side": "buy",
            "product_id": str(self.tradedItem)+"-USD",
            "type": "market"
        }
        buyInfo = json.dumps(buyInfo)
        buyRequest = requests.post(self.api_url + 'orders', auth=self.auth, data=buyInfo)

        messageTexter("Attempting to buy. Waiting for transaction to complete.")
        while True:
            if self.getUSDBalance() < currentMoney or currentCoin > self.getCoinBalance():
                break
            time.sleep(30)

        messageTexter("I bought " + str(self.tradedItem) + " for " + str(self.getPreviousBuyPrice()) + " with " + str(currentMoney))


    def getUSDBalance(self):
        js = requests.get(self.api_url + 'accounts', auth=self.auth).json()
        for item in js:
            if item['currency'] == 'USD':
                return float(item['available'])


    def getCoinBalance(self):
        js = requests.get(self.api_url + 'accounts', auth=self.auth).json()
        for item in js:
            if item['currency'] == str(self.tradedItem):
                return float(item['available'])


    def setPreviousSellPrice(self, newSellPrice):
        fees = requests.get(self.api_url + 'fees', auth=self.auth).json()
        self.previousSellPrice = newSellPrice * (1 - fees['taker_fee_rate'])


    def setPreviousBuyPrice(self, newBuyPrice):
        fees = requests.get(self.api_url + 'fees', auth=self.auth).json()
        self.previousBuyPrice = newBuyPrice * (1 + float(fees['taker_fee_rate']) * 2)