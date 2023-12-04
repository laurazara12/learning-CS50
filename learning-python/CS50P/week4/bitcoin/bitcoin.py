import requests
import sys

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        bitcoin_price = data['bpi']['USD']['rate_float']
        return bitcoin_price
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def calculate_cost(bitcoin_amount):
    try:
        bitcoin_amount = float(bitcoin_amount)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    cost_in_usd = bitcoin_price * bitcoin_amount
    formatted_cost = "{:,.4f}".format(cost_in_usd)
    print(f"The cost of {bitcoin_amount:,} Bitcoins is ${formatted_cost}")

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    calculate_cost(sys.argv[1])

if __name__ == "__main__":
    main()
