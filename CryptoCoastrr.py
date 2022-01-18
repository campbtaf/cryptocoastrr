"""
Authors: Timothy Campbell, Ryan Mulkey, Robert Beery III

Description: Crypto Coaster is a cryptocurrency trader that focuses on trading
             without losing money (hopefully) by riding the Roller Coaster of the market.
             It is as risk free as the creators could make it. It uses a text based interface.

Modified: 7/26/21
"""
import os
import sys
import time

from TRRadeAlgo import TRRadeAlgo

def main():

    print("Welcome to Crypto Coastrr! We're so glad you're using our Program. "
                  "\nPlease read our README.md for information on how to use this program. ")

    if not os.path.isfile('config.json'):
        jsonFout = open('config.json', 'w')
        jsonFout.write('{\n\t"name": "cryypto-coastrr",'
                        '\n\t"version": "1.0.0",'
                        '\n\t"interval": "60",'
                        '\n\t"intermediate-cars": "1",'
                        '\n\t"coin": "BTC",'
                        '\n\n\t"api_key": "",'
                        '\n\t"secret":"",'
                        '\n\t"passphrase": "",'
                        '\n\n\t"phone_number_email": "",'
                        '\n\t"api_url": "https://api.pro.coinbase.com/"\n}')
        jsonFout.close()
        print("We didn't find a config.json file filled out with your information. We created it for you as an"
                 " initializing step."
                 "\nFirstly: Please fill out the config.json file with your API Key, API Secret, and passphrase. "
                 "\nSecondly: Please rerun the program with your new settings saved. "
                 "\nFor more information about this program, and how to fill out your config.json file, please read our"
                 " README.md file."
              "\nYou may safely close this window. It will automatically close in 60 seconds")
        time.sleep(60)
        sys.exit()
    else:
        TRRadeAlgo()



main()