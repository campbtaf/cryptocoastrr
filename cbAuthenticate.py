"""
Authors: Ryan Mulkey, Timothy Campbell, Robert Beery III

Description: Implements an authenticator that allows the program to submit API
requests to coinbase

Date Modified: 7/26/21
"""
import hmac, time, hashlib, base64
from requests.auth import AuthBase


# Create custom authentication for Coinbase API
class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = bytes(str(timestamp + request.method + request.path_url + (request.body or '')), 'latin-1')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, digestmod = hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request