import requests
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
api_key = os.getenv("CMC_API_KEY")

# Portfolio data
portfolio = {
    "BTC": 0.5,
    "ETH": 2,
    "ADA": 500
}

# Purchase prices
purchase_prices = {
    "BTC": 25000,
    "ETH": 1800,
    "ADA": 0.30
}

# CoinMarketCap API Request URL
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

def fetch_data():
    try:
        # Send the request to CoinMarketCap API
        response = requests.get(url, headers=headers)

        # Check if the response status code is 200 (successful request)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None

def display_portfolio(data):
    if data is None:
        print("No data available to display.")
        return

    total_value = 0
    total_profit_loss = 0

    print("==== Crypto Portfolio ====\n")
    for currency in data["data"]:
        symbol = currency["symbol"]
        if symbol in portfolio:
            price = currency["quote"]["USD"]["price"]
            amount = portfolio[symbol]
            bought_price = purchase_prices[symbol]

            value = price * amount
            profit_loss = (price - bought_price) * amount

            total_value += value
            total_profit_loss += profit_loss

            print(f"{symbol}:")
            print(f"  Price Now     : ${price:.2f}")
            print(f"  Amount Owned  : {amount}")
            print(f"  Value         : ${value:.2f}")
            print(f"  Profit/Loss   : ${profit_loss:.2f}\n")

    print("==== Summary ====")
    print(f"Total Portfolio Value : ${total_value:.2f}")
    print(f"Total Profit/Loss     : ${total_profit_loss:.2f}")
    print("\n-------------------------\n")

def live_update():
    while True:
        print("Fetching data...")
        data = fetch_data()  # Fetch latest data
        display_portfolio(data)  # Display portfolio values
        time.sleep(60)  # Wait for 60 seconds before fetching the data again

if __name__ == "__main__":
    live_update()

