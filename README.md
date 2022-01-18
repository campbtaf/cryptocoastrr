# Crypto-Coastrr

Crypto Coaster is a cryptocurrency trader that focuses on trading without losing money (hopefully) by riding the Roller 
Coaster of the market. It is as risk free as the creators could make it. It uses a text based interface. To run the program, run the file CryptoCoasterr.py. Before running, make sure to enter all required data into config.json. A coinbase pro or sandbox account is required to use this program.

## config.json

Your information must be put into the config.json file before the program can run. If you run the program without any 
config.json file present, Crypto-Coastrr will create a new file. In which, you can then fill in your information. 
**Config.json should be present inside the folder containing the Crypto-Coastrr executable.**

### Example json format for config.json:

    {
        "name": "cryptocoastrr",
        "version": "1.0.0",

        "interval": "60",
        "intermediate-cars": "1",
        "coin": "BTC",
        
        "api_key": "Enter your API key here",
        "secret":"Enter your secret key here",
        "passphrase": "Enter your Coinbase Pro passphrase",
        "phone_number_email": "phone_number@carrier_extension"
        "api_url": "url"
    }

## Components of the config file:

### interval:
    
This is the time (in seconds) between calls to the Coinbase API

### intermediate-cars:

All coasters have 2 cars initially - an engine and a caboose. Intermediate-cars represents the amount of cars 
between the engine and caboose. For example, 1 intermediate car would create a coaster in
the format of C - I - E, where C is the caboose, I is an intermediate car, and E is the engine. 

### coin:

This indicates which cryptocurrency you are trading on Coinbase.  Options are:

    ALGO, DASH, OXT, ATOM, KNC, MIR, REP, ICP, CGLD, COMP, NMR, OMG, BAND, XLM, EOS, ZRX, BAT, UNI, YFI, LRC, MANA, REN,
    LINK, BTC, BAL, LTC, USD, ETH, BCH, ETC, ZEC, NU, FIL, AAVE, SNX, BNT, SUSHI, MLN, ANKR, CRV, STORJ, SKL, AMP,
    1INCH, ENJ, NKN, OGN, FORTH, GTC, TRB, XTZ, CTSI, MKR, UMA, DOGE, ADA, DOT, CHZ, SOL, BOND, LPT, QNT, KEEP, RLY, 
    MASK, MATIC, CLV, FET

### api_key:

The API key allows this program to interact with your Coinbase account.  If you want to test in sandbox mode, you will
need to generate a sandbox API key.

### secret:

The secret is the API secret given to you when you create your API Key on Coinbase Pro (or Coinbase Pro Sandbox). This 
is only given once at the time of creation. 

### passphrase:

This is the passphrase used during the creation of your API Key on Coinbase Pro (or Coinbase Pro Sandbox).

### phone_number_email:

To enable text messaging you must fill in the empty quotes of section "phone_number_email".
Pick a carrier in the format of 'your_phone_number@carrier_extension'. For example, if your carrier
is `AT&T` and you number is `1234567890`, you would enter `1234567890@txt.att.net`. If your extension is
not listed below, you will need to look one up for your carrier.

    T-Mobile - @tmomail.net
    Virgin Mobile - @vmobl.com
    AT&T - @txt.att.net
    Sprint - @messaging.sprintpcs.com
    Verizon - @vtext.com
    Tracfone - @mmst5.tracfone.com
    Ting - @message.ting.com
    Boost Mobile - @myboostmobile.com
    U.S. Cellular - @email.uscc.net
    Metro PCS - @mymetropcs.com

### api_url:

API url can be either the Coinbase Pro API (for real world trading), or the Coinbase Sandbox API
(for testing variations of the config files).

    Coinbase Pro API - https://api.pro.coinbase.com/
    Sandbox API - https://api-public.sandbox.pro.coinbase.com/
