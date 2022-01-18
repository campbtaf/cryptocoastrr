# This file is obsolete
# See TRRadeAlgo.py for most up to date version
from priceHistory import priceHistory
from price import CBPrice as price
from highPrice import highPrice
from lowPrice import lowPrice
from avgLowPrice import avgLowPrice
from avgHighPrice import avgHighPrice
from BTCTrader import BTCTrader
import time
import json


def lowHighBTCTrader():

    balance = 100

    btcTrader = BTCTrader(balance)
    btcTrader.setTradingItem('BTC-USD')
    priceHist = priceHistory(btcTrader.getTradingItem())

    # sorting the 2d list from highest to lowest for each lowest_value and highest_value

    highestValue = highPrice(priceHist)
    lowestValue = lowPrice(priceHist)
    highestAverage = avgHighPrice(priceHist)
    lowestAverage = avgLowPrice(priceHist)

    #load config.json as a dictionary
    jsonFin = open('./crypto-trader/config.json', 'r')
    jsonData = json.load(jsonFin)
    jsonFin.close()

    currencyOwned = btcTrader.canTrade()
    print(currencyOwned)

    if currencyOwned == 'BTC-USD':
        owned = True
    else:
        owned = False

    cars = []
    for i in range(int(jsonData.get("intermediate-cars")) + 1):
        cars.append(price())
        time.sleep(30)
    while True:
        cars.append(price())
        if not owned: #buy
            if (cars[-1] < btcTrader.getPreviousSellPrice()) or (btcTrader.getPreviousSellPrice() == 0.00):

                if sorted(cars) == cars:
                    btcTrader.setPreviousBuyPrice(price())
                    btcTrader.buy()
                    owned = True
                else:
                    print("less than previous sell price but dropping. no buy.")
            else:
                print("head greater than previous sell price but dropping. no buy.")

        elif owned: #sell
            if cars[-1] > btcTrader.getPreviousBuyPrice():
                carSort = cars.copy()
                carSort.sort(reverse=True)
                if carSort == cars:
                #if reversed(sorted(cars)) == cars:
                    btcTrader.setPreviousSellPrice(price())
                    btcTrader.sell()
                    owned = False
                else:
                    print("greater than previous buy price but gaining. no sell.")
            else:
                print("at a loss. holding fast. not selling")
        else:
            print('nothing happened')
        print(cars)
        cars.pop(0)
        time.sleep(int(jsonData.get("interval")))


if __name__ == '__main__':
    lowHighBTCTrader()