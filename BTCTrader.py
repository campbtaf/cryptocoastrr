from Trader import Trader
import json, requests, time
from cbAuthenticate import CoinbaseWalletAuth
from messageTexter import messageTexter


class BTCTrader(Trader):

    def __init__(self):
        Trader.__init__(self)

        jsonFin = open('config.json', 'r')
        jsonData = json.load(jsonFin)
        jsonFin.close()

        #self.api_url = 'https://api.pro.coinbase.com/' # Coinbase Pro API
        self.api_url = 'https://api-public.sandbox.pro.coinbase.com/' # Sandbox API
        self.auth = CoinbaseWalletAuth(jsonData.get("api_key"), jsonData.get("secret"), jsonData.get("passphrase"))
        self.tradedItem = jsonData.get("coin")


    def sell(self):
        currentMoney = self.getUSDBalance()
        currentBTC = self.getBTCBalance()
        sellInfo = {
            "size": str(currentBTC),
            "side": "sell",
            "product_id": "BTC-USD",
            "type": "market"
        }
        sellInfo = json.dumps(sellInfo)
        sellRequest = requests.post(self.api_url + 'orders', auth=self.auth, data=sellInfo)
        print("Attempting to sell. Waiting for transaction to complete.")
        messageTexter("\nAttempting to sell. Waiting for transaction to complete.")
        while True:
            if self.getUSDBalance() > currentMoney or currentBTC < self.getBTCBalance():
                break
            time.sleep(30)
        print("I sold bitcoin for ", self.getPreviousSellPrice(), " and now have ", self.getUSDBalance(), '.')
        messageTexter("\nI sold bitcoin for " + str(self.getPreviousSellPrice()) + " and now have " + str(self.getUSDBalance()) + '.')


    def buy(self):
        currentMoney = self.getUSDBalance()
        currentBTC = self.getBTCBalance()
        buyInfo = {
            "size": round(currentMoney, 8),
            "side": "buy",
            "product_id": "BTC-USD",
            "type": "market"
        }
        buyInfo = json.dumps(buyInfo)
        buyRequest = requests.post(self.api_url + 'orders', auth=self.auth, data=buyInfo)
        print("Attempting to buy. Waiting for transaction to complete.")
        messageTexter("\nAttempting to buy. Waiting for transaction to complete.")
        while True:
            if self.getUSDBalance() < currentMoney or currentBTC > self.getBTCBalance():
                break
            time.sleep(30)
        print("I bought bitcoin for ", self.getPreviousBuyPrice(), " with ", currentMoney)
        messageTexter("\nI bought bitcoin for " + str(self.getPreviousBuyPrice()) + " with " + str(currentMoney))


    def getUSDBalance(self):
        js = requests.get(self.api_url + 'accounts', auth=self.auth).json()
        for item in js:
            if item['currency'] == 'USD':
                return float(item['available'])


    def getBTCBalance(self):
        js = requests.get(self.api_url + 'accounts', auth=self.auth).json()
        for item in js:
            if item['currency'] == 'BTC':
                return float(item['available'])


    def setPreviousSellPrice(self, newSellPrice):
        self.previousSellPrice = newSellPrice #* (1 + float(fees['taker_fee_rate']) * 2)


    def setPreviousBuyPrice(self, newBuyPrice):
        fees = requests.get(self.api_url + 'fees', auth=self.auth).json()
        self.previousBuyPrice = newBuyPrice * (1 + float(fees['taker_fee_rate']) * 2)