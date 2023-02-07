# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import talib
from talib.abstract import *
# mplfinance 绘图
#import mplfinance as mpf

for f in talib.get_function_groups():
    print(f)

    print('talib总共有{}个函数！'.format(len(talib.get_functions())))

    for group, func in talib.get_function_groups().items():
        print(group)
        print('-----------------------')
        for func in func:
            print(func)
        print()

print(MA, "\n---------------------\n")
print(SMA, "\n---------------------\n")
print(EMA, "\n---------------------\n")
print(WMA, "\n---------------------\n")
print(DEMA, "\n---------------------\n")
print(TEMA, "\n---------------------\n")
print(KAMA, "\n---------------------\n")
prices = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
print(prices)
sma5 = talib . SMA(np . array(prices), 5)
print(sma5)
ema5 = talib. EMA(np . array(prices), 5)
print(ema5)
wma5 = talib . WMA(np . array(prices), 5)
print(wma5)
dema2 = talib. DEMA(np. array(prices), 2)
print(dema2)
tema2 = talib. TEMA(np . array(prices), 2)
print(tema2)
kama5 = talib . KAMA(np. array(prices), 5)

print("TA- LIB MACD指标及其使用------------------------\n")
print(MACD)
#计算案例
series=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0 ,7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
macd,macdsignal, macdhist=talib.MACD(np . array(series ),fastperiod=3, slowperiod=6, signalperiod=3)
print(macd, macdsignal, macdhist)
print("TA- LIB RSI指标及其使------------------------\n")
print(RSI)
rsi6=talib . RSI (np . array(series ) ,timeperiod=6)
rsi12=talib. RSI(np . array( series ),timeperiod=12)
print(rsi6, rsi12)
print("TA- LIB布林带指标及其使用----------\n")
print ( BBANDS)
#计算案例
upperband, middleband, lowerband=talib . BBANDS(np . array( series) ,timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
print (upperband, middleband, lowerband)
print("TA-LIB OBV指标及其使用: --------------------------\n") 
print(OBV)
#计算案例
prices=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0 ,7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
volumes=[55.0, 98,1000,10, 20, 30, 500, 10000, 3, 2, 1, 1, 1, 1, 5,10]
obv=talib.OBV(np . array(prices), np . array(volumes))
print (obv)

apple_df = pd.read_csv('../data/AAPL.cCSV', index_col=0, parse_dates=True)

print(apple_df.head())
kwargs=dict(
type= 'candle',
volume=True, 
ylabel='Price',
ylabel_lower= ' volume ',
figratio=(1200/72,480/60),
figscale=3,
datetime_format= ' %Y %m-%d',
xrotation=0
)

my_color=mpf . make_marketcolors(
up='red',
down= ' limegreen',
edge= ' inherit',
wick= ' inherit',
volume= ' inherit '
)

my_style=mpf.make_mpf_style( 
marketcolors=my_color,
figcolor= ' #EEEEE' ,
y_on_right=False,
gridaxis= 'both',
gridstyle='-.',
gridcolor= '#E1E1E1',
)

sma30=talib.SMA(apple_df['Close' ], 30)
wma30=talib.WMA(apple_df['Close'],30)
dema30=talib.DEMA(apple_df[ 'close' ],30)
tema30=talib.TEMA( apple_df[ 'close'], 30)

sma30=pd.DataFrame (sma30, columns=['0' ])
wma30=pd .DataFrame (wma30, colunns=['0'])
dema30=pd. DataFrame(dema30, columns=['e'])
tema30=pd.DataFrame(tema30, columns=[ '0' ])

macd , macdsignal, macdhist=talib.MACD(apple_df[ 'Close'])
macd=pd.DataFrame(macd, columns=[ 'O'])
macdsignal=pd.DataFrame (macdsignal, columns=['0' ])
macdhist=pd .DataFrame (macdhist, colunns=['0' ])

slowK,slowD=talib.STOCH(apple_df['High'], apple_df['Low'], apple_df['close'])
slowK=pd .DataFrame(slowK, columns=['0' ])
slowD=pd .DataFrame(slowD, columns=['o'])

add_plot=[
mpf.make_addplot(sma30 . tail(160),color= 'red'),
mpf.make_addplot (wma30. tail( 160) , color= 'green'),
mpf.make_addplot( dema30. tail(160) , color='blue'),
mpf.make_addplot (tema30. tail(160),color='purple'),
mpf.make_addplot(macd. tail(160),panel=2),
mpf.make_addplot (macdsignal. tail(160),panel=2),
mpf.make_addplot (macdhist. tail(160),panel=2),
mpf.make_addp1ot(slowK. tail(160),panel=3),
mpf.make_addplot( slowD. tail(160),panel=3),
]

mpf. plot(apple_df. tail(160),**kwargs, style=my_style, addplot=add_plot)