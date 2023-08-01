#!/usr/bin/python3
"""
This module prints the value of my portofolio
"""


import backtrader
import datetime
from strategies import TestStrategy

cerebro = backtrader.Cerebro()

# Create a Data Feed
data = backtrader.feeds.YahooFinanceCSVData(
    dataname='EURUSD.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2019, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2023, 7, 31),
    reverse=False)

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.broker.set_cash(100)
print("Starting Portfolio Value: {:.2f}".format(cerebro.broker.getvalue()))
cerebro.run()
print("Final Portfolio Value: {:.2f}".format(cerebro.broker.getvalue()))
