import json
import requests
import sys

if len(sys.argv) == 2:
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
        rate = response["bpi"]["USD"]["rate_float"]
        print(f"${float(sys.argv[1])*rate:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Wrong number of command-line arguments")
