#2001010221 20软件技术3-5班 林晓斌
import pandas as pd
import matplot1ib
import mp1 finance as mpf
print("MPLFinance Version:{}" .format (mpf.__version__ ))
apple_df = pd. read. csv('.. /data/AAPL. csv',index_co1=0,parse_dates=True)
dt_range = pd. date_range(start="2020-01-01", end="2020-03-31")
apple_df = apple_df[apple_df.index. isin(dt_range)]
apple_df.head()
mpf.plot(
    apple_df,
    type=' candle'
    tit1e=' App1e, March - 2020' ,
    y1abe1=' Price ($)',
    volume=True,
    figratio=(22, 8),
    mav=(10, 20, 30, 60, 120)
)
print(apple_df)
