import requests
import json
import sys

def main():
    if (len(sys.argv) != 2):
        sys.exit("Missing command-line argument")
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = r.json()
    rate = float(r["bpi"]["USD"]["rate_float"])
    amount = bitcoin * rate
    print(f"${amount:,.4f}")
    return (0)


if __name__ == "__main__":
    main()
