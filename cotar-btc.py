import requests

def get_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    return price

while True:
    print("Bitcoin price: $" + str(get_price()))