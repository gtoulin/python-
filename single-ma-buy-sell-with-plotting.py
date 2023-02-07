# 单均线交易策略--绘制图形功能
import datetime # For datetime objects
import backtrader as bt
#创建策略


class SingleMaStrategy (bt. Strategy):
# 策略参数
  params = (
    ('ma_ period', 15),  # 均线周期
    )
  def log(self, txt, dt=None):
    dt=dt or self. datas[0]. datetime. date(0)
    print(' % s,% s' % (dt. isoformat(),txt))
  
  def __init__(self):
# 收盘价数据集
    self. dataclose=self. datas[0]. close
# 订单状态.
    self. order=None
    self. buyprice=None
    self. buycommn=None
# 添加均线指标
    self. sma=bt. indicators. SimpleMovingAverage(
    self. datas[0],period=self. params.ma_period)
# 绘图指标
    bt. indicators. ExponentialMovingAverage(self. datas[0],period=25)
    bt. indicators. WeightedMovingAverage(self. datas[0],period=25, subplot=True)
    bt. indicators. StochasticSlow(self. datas[0])
    bt. indicators. MACDHisto(self. datas[0])
    rsi=bt. indicators. RSI(self. datas[0])
    bt. indicators. SmoothedMovingAverage(rsi,period=10)
    bt. indicators. ATR(self. datas[0],plot=False)

# 订单通知
  def notify_order(self, order):
    if order. status in [order. Submitted, order. Accepted]:
# 如果订单状态是提交/接受，直接返回
      return
# 检查订单是否已完成，现金不足会拒绝订单
    if order. status in [order. Completed]:
      if order. isbuy():
        self. log('BUY EXECUTED, Price: % . 2f,Cost: % . 2f,Comm: % . 2f'% (order. executed. price))
        self. buyprice=order. executed. price
        self. buycomm=order. executed. comm
      elif order. issell():
        self. log('SELL EXECUTED, Price: % . 2f,Cost: % . 2f,Comm: % . 2f'% (order. executed. price))
        self. bar_executed=len(self)
    elif order. status in [order. Canceled, order. Margin, order. Rejected]:
        self. log('Order Canceled/Margin/Re jected')
# 设置为无待办订单
        self. order=None

# 交易通知
    def notify_trade(self, trade):
      if not trade. isclosed:
        return
      self. log('交易毛利润: % . 2f,净利润: % . 2f'% (trade. pnl,trade. pnlcomm))
    
    def next(self):
# 打印当前收盘价
        self. log('Close,% .2f' % self. dataclose[0])

# 检查是否已有订单，如果有直接返回，防止重复下单
        if self. order:
          return
# 检查是否有头寸
        if not self. position:
# 没有头寸则尝试买
          if self. dataclose[0] > self. sma[0]:
# 买
            self. log(' BUY CREATE, % .2f' % self. dataclose[0])
# 修改订单状态为
          self. order=self. buy()
        else:
# 已有头寸，尝试卖(买后持有5个时段卖出)
          if self. dataclose[0] < self. sma[0]:
# 卖出
            self. log('SELL CREATE,% .2f' % self. dataclose[0])
# 修改订单状态
            self. order=self. sell()

if __name__=='__main__':
# Create a cerebro entity
  cerebro=bt. Cerebro()
# Add a strategy
  cerebro. addstrategy(SingleMaStrategy,ma_period=35)

  data=bt.feeds.GenericCSVData(
  dataname='.. / data/AAPL. csv',
  datetime=0,
  open=1,
  high=2,
  low=3,
  Close=4,
  volume=6,
  dtformat=('%Y-%m-%d'),
  fromdate=datetime. datetime(2019, 1, 1),
  todate=datetime. datetime(2020, 12, 31)
  )
# Add the Data Feed to Cerebro
  cerebro. adddata(data)
# 设置处置资金
  cerebro. broker. setcash(100000.0)

# 设置佣金
  cerebro. broker. setcommission(0.001)
  cerebro. addsizer(bt. sizers. FixedSize,stake=100)
# Print out the starting conditions
print('初始市值: % . 2f'% cerebro. broker. getvalue())
# Run over everything
cerebro. run()
# Print out the final result
print('最终市值: % .2f'% cerebro. broker. getvalue())
cerebro. plot()
