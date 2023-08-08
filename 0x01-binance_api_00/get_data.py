#!/usr/bin/python3
import config, csv
from binance import Client

client = Client(config.API_KEY, config.API_SECRET)

#prices = client.get_all_tickers()

#for price in prices:
#    print(price)

#candles = client.get_klines(symbol='XMRUSDT', interval=Client.KLINE_INTERVAL_4HOUR)

candles = client.get_historical_klines("XMRUSDT", Client.KLINE_INTERVAL_4HOUR, "1 Jan, 2017", "7 Aug, 2023")

#csvfile = open('XMRUSDT_4H.csv','w',newline='')
csvfile = open('XMRUSDT_2017-23_4H.csv','w',newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
#    print(candlestick)
    candlestick_writer.writerow(candlestick)

csvfile.close()
print(len(candles))
