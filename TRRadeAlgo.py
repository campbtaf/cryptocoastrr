"""
Authors: Ryan Mulkey, Timothy Campbell, Robert Beery III

Description: This is the algorithm for trading using the cryptoTrader object. It trades simply by following the rise
             and fall of the market and waits for a clear rise or fall to buy or sell respectively.

Date Modified: 7/27/21

"""


from price import CBPrice as price
from cryptoTrader import cryptoTrader
import time, json
from messageTexter import messageTexter


def TRRadeAlgo():

    # load config.json as a dictionary
    jsonFin = open('config.json', 'r')
    jsonData = json.load(jsonFin)
    jsonFin.close()

    cryptTrader = cryptoTrader()

    lossHellCounter = 0
    cars = []
    interval = int(jsonData.get("interval"))
    intermediateCars = int(jsonData.get("intermediate-cars"))
    messageTexter("Initiating Crypto Coaster" +
                  "\ninterval: " + str(interval) +
                  "\nintermediate cars: " + str(intermediateCars))
    for i in range(intermediateCars + 1):
        cars.append(price())
        time.sleep(interval)

    messageTexter("current account USD bal: " + str(cryptTrader.getUSDBalance()) + "\ncurrent account BTC bal: " + str(
        cryptTrader.getCoinBalance()))

    if cryptTrader.getCoinBalance() >= 0.0001:
        owned = True
    else:
        owned = False

    while True:
        cars.append(price())
        if not owned:  # buy
            if (cars[-1] < cryptTrader.getPreviousSellPrice()) or (cryptTrader.getPreviousSellPrice() == 0.00):

                condString = ""
                for car in cars:
                    condString += str(car) + " < "

                if eval(condString[:-3]):
                    cryptTrader.setPreviousBuyPrice(price())
                    cryptTrader.buy()
                    owned = True
                # else:
                # print("not /. no buy.")
            # else:
            # print("greater than previous sell price. no buy.")

        elif owned:  # sell
            if cars[-1] > cryptTrader.getPreviousBuyPrice():

                condString = ""
                for car in cars:
                    condString += str(car) + " > "

                if eval(condString[:-3]):  # if all values are in a \ line.
                    cryptTrader.setPreviousSellPrice(price())
                    cryptTrader.sell()
                    owned = False
                elif (lossHellCounter >= 2):  # if we're in lossHell
                    cryptTrader.setPreviousSellPrice(price())
                    cryptTrader.sell()
                    owned = False
                    cryptTrader.setPreviousSellPrice(0.00)
                # else:
                # print("not \. no sell.")

                lossHellCounter = 0

            else:
                if lossHellCounter <= 1:
                    # print("at a loss. holding fast. not selling. Hopefully not entering Loss-Hell.")
                    lossHellCounter += 1
                # stop Loss Hell at a loss (loss Hell exit sell)
                # elif lossHellCounter >= 5:
                # cryptTrader.setPreviousSellPrice(price())
                # cryptTrader.sell()
                # owned = False
                # cryptTrader.setPreviousSellPrice(0.00)
                # lossHellCounter = 0
                else:
                    # print("You're in Loss-Hell!")
                    lossHellCounter += 1
        # else:
        # print('nothing happened')
        # print(cars)
        cars.pop(0)
        time.sleep(interval)


if __name__ == '__main__':
    TRRadeAlgo()
