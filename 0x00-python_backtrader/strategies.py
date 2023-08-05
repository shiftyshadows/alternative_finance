#!/usr/bin/python3
"""
   This module defines a class with  a test strategy.
"""


import backtrader
import datetime


# Create a Strategy
class TestStrategy(backtrader.Strategy):

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print("{:s}, {:s}".format(dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXECUTED {n}'.format(order.executed.price))
            self.bar_executed = len(self)
        self.order = None

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log("Close, {:.2f}".format(self.dataclose[0]))

        if self.position:
            return
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    self.log("BUY CREATED, {:.2f}".format(self.dataclose[0]))
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + 5):
                #Simply log the closing price of the series from the reference
                self.log('SELL CREATED {:.2f}'.format(self.dataclose))
                self.order = self.sell()




