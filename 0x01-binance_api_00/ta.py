#!/usr/bin/python3
import talib
from numpy import genfromtxt

my_data = genfromtxt('XMRUSDT_4H.csv', delimiter=',')

close = my_data[:,4]

print(close)

RSI = talib.RSI(close)

print(RSI)
