#A program that will generate the current price of bitcoin at the quantity specified by the user via command line argument.

import sys
import requests
import json

#Get value from command line
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

#Get current price of bitcoin
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total = bitcoin * value
    print(f"${total:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)