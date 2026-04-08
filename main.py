import requests
import numpy as np
url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",   
    "interval": "1d",      
    "limit": 5             
}
response = requests.get(url, params=params)

data =np.array(response.json())
data=data[:,0:6]
attributes = ['open time','o','h','l','c','v']
for i,candle in enumerate(data):
    print("=====")
    print(f"c{i}")
    for i,att in enumerate(candle):
        print(f"[{attributes[i]}]->[{att}]")