#!/usr/bin/python3
"""
   This module defines a class with  a test strategy.
"""


import backtrader
import datetime


# Create a Strategy
class TestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print("{:s}, {:s}".format(dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log("Close, {:.2f}".format(self.dataclose[0]))

        if self.dataclose[0] < self.dataclose[-1]:
            if self.dataclose[-1] < self.dataclose[-2]:
                self.log("Buy Create, {:.2f}".format(self.dataclose[0]))
                self.buy()
