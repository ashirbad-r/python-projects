# Crypto Portfolio Tracker using CoinMarketCap API

This is a Python project that tracks your cryptocurrency portfolio using real-time data from the CoinMarketCap API. It calculates the current value of your holdings and shows your profit or loss based on your purchase price.

## Features

- Fetch real-time cryptocurrency prices
- Track portfolio value and profit/loss
- Secure API key storage using `.env`
- Customizable coin holdings and purchase prices

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

Install requirements using:


## Folder Structure

CryptoPortfolioTracker/ 
├── .env 
├── main.py 
├── requirements.txt 
└── README.md

## How to Set Up

1. Clone the repository and navigate into it:


## How to Set Up

1. Clone the repository and navigate into it:

git clone https://github.com/yourusername/CryptoPortfolioTracker.git cd CryptoPortfolioTracker


2. Create a `.env` file and add your CoinMarketCap API key:

CMC_API_KEY=your_coinmarketcap_api_key


You can get your API key from: https://coinmarketcap.com/api/

3. Edit your portfolio and purchase prices in `main.py`:

```python
portfolio = {
    "BTC": 0.5,
    "ETH": 2,
    "ADA": 500
}

purchase_prices = {
    "BTC": 25000,
    "ETH": 1800,
    "ADA": 0.30
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

How to Run:

python3 main.py

