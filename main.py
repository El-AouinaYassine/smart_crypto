import requests

url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",   
    "interval": "1d",      
    "limit": 5             
}
response = requests.get(url, params=params)

data = response.json()

for i,candle in enumerate(data):
    print("=====")
    print(f"c{i}")
    for att in candle:
        print(f"->{att}")