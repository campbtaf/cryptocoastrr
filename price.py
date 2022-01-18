"""
Authors: Timothy Campbell, Ryan Mulkey, Robert Beery III

Description: This script uses our coinbase authenticator to retrieve the bitcoin
price from coinbase in realtime for use with the trading algorithm.

Modified: 7/27/21
"""
import requests
import json
from cbAuthenticate import CoinbaseWalletAuth

def price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    price = data["bpi"]["USD"]["rate"]

    return float(price.replace(',', ''))


def CBPrice():
    jsonFin = open('config.json', 'r')
    jsonData = json.load(jsonFin)
    jsonFin.close()

    api_url = jsonData.get("api_url")
    auth = CoinbaseWalletAuth(jsonData.get("api_key"), jsonData.get("secret"), jsonData.get("passphrase"))

    ## Get current price
    r = requests.get(api_url + 'products/' + str(jsonData.get('coin')) + '-USD/ticker', auth=auth)
    price = r.json().get('price')


    return float(price)