#!python3

import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpl
import matplotlib.dates as mdates

style.use('ggplot')

'''
Downloading dataset from yfinance of Tesla  - 

import yfinance as yf

tsla = yf.Ticker('TSLA')
tsla.history('1m')
data = yf.download('TSLA', period = '5y')
data.to_csv('tsla.csv')

'''

#reading data from csv file 
df = pd.read_csv('tsla.csv', index_col = 0, parse_dates = True)

#Resampling for Candlestick graph using Adj. Close and Volume

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum()

mpl.plot(df_ohlc, type = 'candle', style = 'yahoo')

