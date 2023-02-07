import datetime
import backtrader as bt

#创建策略均线EMA斜率交易策略
class DualEmaslopestrategy (bt . strategy):
#策略参数
  params = (
  ('fast_ period', 15), #快均线周期
  ('slow_ period', 60), #慢均线周期
  ('slope_ period', 7), #计算斜率的周期
  ('print_1og', False),
)
  def log(self, txt, dt=None):

    '''Logging function fot this strategy'''
    dt = dt or self .datas [0]. datetime . date(0) 
    if(self . params . print_1og==True):
      print( '%s,%s' % (dt. isoformat(), txt))

  def __init__ (self):
#收盘价数据集
    self .dataclose = self . datas[0].close
#添加均线指标
    self . fast_ema=bt. talib. EMA(self . dataclose, timeperiod=self . params. fast_period )
    self .slow_ema=bt. talib . EMA(self . dataclose, timeperiod=self . params . slow_period)
    self.fast_ema_slope=bt.talib.LINEARREG_SLOPE(self.fast_ema, timeperiod=self . params. slope_period)
    self .slowema_slope=bt.talib. LINEARREG_SLOPE(self .slow_ema, timeperiod=self . params. slope_period)

#订单状态
    self .order = None
    self . buyprice=None
    self . buycomm=None
#订单通知
  def notify_order(self, order):
    if order . status in [order . submitted, order . Accepted]:
#如果订单状态是提交/接受，直接返回
      return

#检查订单是否已完成，现金不足会拒绝订单
  if order.status in [order.Completed]:
    if order . isbuy(): 
      self.log( 'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order . executed. price, order . executed . value, order . executed . comm) )
      self . buyprice=order . executed . price
      self . buycomm=order . executed . comm
    elif order .issell():
      self . log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order . executed . price, order . executed. value, order . executed. comm) )
      self . bar_executed = len(self)
    
  elif order . status in [order. Canceled, order .Margin, order . Rejected]: 
      self . log( 'order Canceled/Margin/ Rejected')

#设置为无待办订单
  self .order = None

#交易通知
  def notify_trade(self, trade):
    if not trade . isclosed:
      return
    self.log( '交易毛利润: %.2f,净利润: %.2f' %(trade. pnl, trade . pnlcomm) )

    def next(self):
#打印当前收盘价
        self .log('Close, %.2f' % self. dataclose[0])
#检查是否已有订单，如果有直接返回，防止重复下单
        if self . order:
          return 

#检查是否有头寸
        if not self . position:
#没有头寸则尝试买
          if self.fast_ema_slope[0]>0 and self.slow_ema_slope[0]>0:
#买
              self .log('BUY CREATE, %.2f' % self .dataclose[o])
#修改订单状态为
              self .order = self . buy()
        else:

#已有头寸，尝试卖(买后持有5个时段卖出)
          if self.fast_ema_slope[0]<0 or self.slow_ema_slope[0]<0:
#卖出
            self.log('SELL CREATE, %.2f' % self .dataclose[0])
#修改订单状态
            self.order = self .sell( )

def run():
  cerebro = bt . Cerebro()
  cerebro . addstrategy(DualEmaSlopestrategy, fast_period=10, slow_period=50, slope_period=7, print_log=True)
  data=bt.feeds.GenericCSVData(
  dataname= ' ../data/AAPl.csv',
  datetime=0,
  open=1,
  high=2,
  low=3,
  close=4,
  volume=6,
  dtformat=('%Y %m %d'), 
  fromdate=datetime . datetime (2019,1,1),
  todate=datetime . datetime ( 2020, 12,31)
  )

#添加数据
  cerebro . adddata(data)
#设置初始资金
  cerebro . broker . setcash(100000.0)
#设置佣金
  cerebro . broker . setcommission(0.001)
  cerebro . addsizer(bt . sizers. Fixedsize, stake=100)
#执行策略
  print('执行前的市值: %.2f' % cerebro. broker . getvalue())
  cerebro. run( )
  print('执行后的市值: %.2f, 收益率: %.2f %' % (cerebro. broker. getvalue(), (cerebro . broker . getvalue()- 100000.0) *100/ 100000.0))
  cerebro. plot( )
if __name__ =='__main__':
# result={} 
# optimize_ cerebro params(result)
# print(result)
  run()
