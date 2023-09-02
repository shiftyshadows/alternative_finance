#!/usr/bin/python3
from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS
import config
import csv
from binance import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET)

app = Flask(__name__)
app.secret_key = b'1+Y\UGs76?"2t@23$'

CORS(app)

@app.route('/')
def index():
    title = 'CoinView'

    account_info = client.get_account()

    balances = account_info['balances']

    exchange_info = client.get_exchange_info()

    symbols = exchange_info['symbols']
#    print(exchange_info)

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
#            timeInForce=TIME_IN_FORCE_GTC,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "Error")
    return redirect('/')

@app.route('/history')
def history():
    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "19th Aug, 2023", "1st Sep, 2023")
    processed_candles =[]
    for data in candles:
        candle = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "close": data[4],
            "low": data[3]
        }

        processed_candles.append(candle)
    return jsonify(processed_candles)

if __name__ == '__main__':
    app.run()
