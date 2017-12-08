import time
import os
import requests
while True: 
    os.system('cls')
    request = requests.get("https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD")
    print request.content[2:-2].split(",")[-4]
    time.sleep(10)