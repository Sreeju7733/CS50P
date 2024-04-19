import requests
import sys
import json

if len(sys.argv) == 2:
    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument not an number")
else:
    sys.exit("No command-line argument found")


try:
    api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass

obj = api.json()
price = obj["bpi"]["USD"]["rate_float"]

amount = price * coins

print(f"${amount:,.4f}")
