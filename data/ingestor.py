import requests
import numpy as np
from datetime import datetime

url = "https://api.binance.com/api/v3/klines"

params = {
    "symbol": "BTCUSDT",   
    "interval": "1h",      
    "limit": 10   
}
response = requests.get(url, params=params)


data =np.array(response.json(),dtype='float')
# btw had data rah Unix Timestamps in milliseconds.
# khass nrdoha humane readable b3da
data=data[:,0:6]
attributes = ['open time','o','h','l','c','v']
data_dict = []
for i,candle in enumerate(data):
    # NEED DATA TO be humane readable b3da
    data_dict.append({'ot':datetime.timestamp((candle[0])/1000),
                      'o':int(candle[1]),
                      'h':int(candle[2]),
                      'l':int(candle[3]),
                      'c':int(candle[4]),
                      'v':int(candle[5])})

for c in data_dict:
    print(c)
    print('\n')
    # break

