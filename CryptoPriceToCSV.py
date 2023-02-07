import requests
import json
from datetime import datetime
import time
import schedule
import csv
import os


def CryptoPrice():
    WavesPriceJson = requests.get('https://wavescap.com/api/asset/WAVES.json').text
    WavesPriceJson1 = float((json.loads(WavesPriceJson)['data']['lastPrice_usdt']))
    WavesPriceJson2 = "{:.4f}".format(WavesPriceJson1)

    PlutoPriceJson = requests.get('https://wavescap.com/api/asset/Ajso6nTTjptu2UHLx6hfSXVtHFtRBJCkKYd5SAyj7zf5.json').text
    PlutoPriceJson1 = float((json.loads(PlutoPriceJson)['data']['lastPrice_usdt']))
    PlutoPriceJson2 = "{:.4f}".format(PlutoPriceJson1)

    XTNPriceJson = requests.get(' https://wavescap.com/api/assets.json').text
    XTNPriceJson1 = float((json.loads(XTNPriceJson)[100]['data']['lastPrice_usdt']))
    XTNPriceJson2 = "{:.4f}".format(XTNPriceJson1)

    now = f"{datetime.now():%Y-%m-%d %H:%M}"

    print(now, WavesPriceJson2, PlutoPriceJson2, XTNPriceJson2)

    file_exists = os.path.exists('CryptoPrice.csv')

    with open('CryptoPrice.csv', 'a', newline='') as file:
        fieldnames = ['Date', 'WAVES', 'PLUTO', 'XTN']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Date':now, 'WAVES':WavesPriceJson2, 'PLUTO':PlutoPriceJson2, 'XTN':XTNPriceJson2})

schedule.every(1).minutes.do(CryptoPrice)

while True:
    schedule.run_pending()
    time.sleep(1)






