import numpy as np
import pandas as pd
import matplotlib. pyplot as plt
#线性回归
from sklearn. linear_model import LinearRegression
#线性脊回归
from sklearn. linear_model import Ridge
#多项式回归
from sklearn . preprocessing import PolynomialFeatures
from sklearn. linear_model import LinearRegression
from sklearn. pipeline import Pipeline
from sklearn. ensemble import RandomForestRegressor
from sklearn import tree
from sklearn import svm
from sklearn. gaussian_process import GaussianProcessRegressor
from sklearn. gaussian_process . kernels import DotProduct, WhiteKernel
#绘图函数
def draw_err(delt):
  plt . figure(figsize=(15, 8))
  plt .plot(delt, color= 'r' ,markersize=1,linestyle='-', label="delt")
  plt. grid(True)
  plt. legend()
  plt. show()
# name 训练的模型名称:
# 1r--线性回归, poly--多项式回归(2次)，ridge---脊 回归
#rf--随机森林回归
# tree--诀策树回归
# svm-支撑向量积回归
# gauss--高斯核回归
def train(name, filename="../ . ./data/if-future-5min-training.csv"):
#使用7日数据预测下一日的收盘价
  training_dataset = pd. read_csv(filename)
  training_data_num=training_dataset. shape[0]
  print("training_ _data_ num:", training_data_num)
  x_train = training_dataset. iloc[:,3:].values #训练集开高低收量5*10=50个特征
  y_train = training_dataset. iloc[:,2].values #训练集第3日收益率

  model=None
  if name=='1r': #线性回归
    model = LinearRegression()
  elif name==' ridge': #脊回归
   model=Ridge( alpha=100.0)
  elif name=='poly': #多项式回归
    model = Pipeline([( 'poly', PolynomialFeatures(degree=2)),('linear', LinearRegression(fit_intercept=False))])
  elif name=='rf': #随机森林回归
   model=RandomForestRegressor()
  elif name=='tree': #决策树回归
   model = tree.DecisionTreeRegressor()
  elif name==' svm': #支撑向量机
   model = svm. SVR()
  elif name== 'gauss': #高斯核回归
   model = GaussianProcessRegressor(kernel=DotProduct(), random_state=0) # kernel = DotProduct() + WhiteKernel()

  if(model!=None):
    model = model.fit(x_train, y_train)
  return model

def test(model, filename="../ ../data/if-future- 5min-test.csv"):
  test_dataset=pd.read_csv(filename )
  test_data_num=test_dataset . shape[0]
  print("test_ data_ num:",test_data_num)
  x_test = test_dataset. iloc[:,3:].values #测试集开高低收量5*7=35个特征
  y_test = test_dataset. iloc[:,2].values #测试集下一日收盘价
  test_pred=model. predict(x_test)
  test_mae=np . mean(np . abs(test_pred-y_test))
  print("预测平均绝对误差: ",test_mae)
  draw_err(test_pred-y_test)

if __name__=='__main__' :
  model=train('1r')
  test (model)


import datetime # For datetime objects
import backtrader as bt
#机器学习回归预测交易策略
class MLPredictStrategy(bt . Strategy):
#策略参数
  params = (
  ('model', None), #模型参赛
  ('print_ 1og', True), #是否打印日志
  )
  def log(self, txt, dt=None):
    '''Logging function fot this strategy'''
    dt = dt or self.datas[0]. datetime . date(0)
    if(self. params.print_log):
      print('%s,%s' % (dt. isoformat(), txt))

  def __int__ (self):
#收盘价数据集
    self .dataclose = self .datas[0]. close
    self.dataopen = self . datas [0]. open
    self . datahigh = self.datas [0].high
    self.datalow = self .datas[0] . low
    self .datavolume = self .datas[0] . volume
#订单状态
    self. order = None
    self. buyprice=None
    self . buycomm=None
    self. totalProfit=0.0
#绘图指标
# bt. indicators . ExponentialMovingAverage(self . datas[0], period=25)
# bt. indicators .WeightedMovingAverage(self . datas[0], period=25， subplot=True)
# bt. indicators . StochasticSlow(self .datas [0])
# bt. indicators .MACDHisto(self. datas[0])
# rsi = bt.indicators . RSI(self .datas[0])
# bt.indicators . SmoothedMovingAverage(rsi, period=10)
# bt. indicators . ATR(self.datas[0], plot=False)
#订单通知
def notify_order(self, order):
  if order.status in [order. Submitted, order . Accepted]:
#如果订单状态是提交/接受，直接返回
    return

#检查订单是否已完成，现金不足会拒绝订单
  if order. status in [order. Completed]:
    if order . isbuy():
      self. log(' BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order . executed. price, order. executed . value, order . executed . comm) )
      self . buyprice=order. executed.price
      self . buycomm=order . executed. comm
    elif order. issell():
      self. log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm: %.2f' % (order. executed . price, order . executed . value, order . executed . comm) )
      self.bar_executed = len(self)
    elif order.status in [order . Canceled, order .Margin, order . Rejected]: 
      self.log('Order Canceled/Margin/Rejected') 
#设置为无待办订单
    self.order = None
#交易通知
def notify_trade(self, trade):
  if not trade . isclosed:
      return
  self. totalProfit+=trade . pn1comm
  self.log(' gross profit: %.2f, net profit: %.2f, total profit: %.2f' %(trade. pnl, trade . pnlcomm,self . totalProfit))

  def next(self):
#打印当前收盘价
      self.log('price, %.2f' % self. dataclose[0])
#检查是否已有订单，如果有直接返回，防止重复下单
      if self . order:
        return

#提取特征
  x=[
      [
      self . dataopen[-1], self. datahigh[-1], self . datalow[-1], self .dataclose[-1], self .datavolume[-1],
      self .dataopen[-2], self.datahigh[-2]， self. datalow[-2], self . dataclose[-2], self . datavolume[-2],
      self.dataopen[-3], self.datahigh[-3], self.datalow[-3], self .dataclose[-3], self . datavolume [-3],
      self . dataopen[-4], self. datahigh[-4], self. datalow[-4], self .dataclose[-4], self .datavolume[-4],
      self.dataopen[-5], self. datahigh[-5], self.datalow[-5], self. dataclose[-5], self .datavolume [-5],
      self . dataopen[-6], self . datahigh[-6], self. datalow[-6], self .dataclose[-6], self .datavolume[-6],
      self .dataopen[-7]，self . datahigh[-7], self .datalcw[-7], self .dataclose[-7], self .datavolume[-7],
      self . dataopen[-8], self. datahigh[-8], self. datalow[-8], self .dataclose[-8], self .datavolume[-8],
      self . dataopen[-9], self . datahigh[-9], self. datalow[-9], self . dataclose[-9], self . datavolume[-9],
      self. dataopen[ -10],self . datahigh[-10],self. datalow[-10],self. dataclose[-10],self .datavo1ume[-10],
      ]
  ]
#使用模型预测回报率
  return_ratio_predicted=self. params . model. predict(x)
  if return_ratio_predicted>0.10: #若预测回报率大于0.10%,则开多
    if self . position. size<0:
      self. order=self. close(exectype=bt . Order. Limit, price=self. dataclose[0]*1.05) #平空仓
      self.log('Close short, %.2f' % self. dataclose[0])
      self . order=self.buy(exectype=bt .Order .Limit, price=self.dataclose[0]*1.05, valid=self.datas[0]. datetime.date(0) + datetime.timedelta(days=1)) #买多
      self.log(' BUY CREATE, %.2f' % self. dataclose[0])
    elif self. position. size==0:
      self . order=self . buy(exectype=bt . Order.Limit, price=self . dataclose [0]*1.05,valid=self . datas[0]. datetime . date(0) + datetime . timedelta(days=1))
      self .log('BUY CREATE, %.2f' % (self. dataclose[0]))
    elif return_ratio_predicted<-0.10: #若预测回报率小于-0.10%,则开空
      if self . position. size>0:
        self. order=self . close(exectype=bt .Order. Limit, price=self . dataclose[0]*0.995) #平多仓
        self.log('Close long, %.2f' % self. dataclose[0])
        self . order=self. sell(exectype=bt . Order .Limit, price=self . dataclose[0]*0.995,valid=self . datas[0]. datetime .date(0) + datetime . timedelta(days=1))
        self .log('SELL CREATE, %.2f' % self. dataclose[0])
      elif self. position. size==0:
        self . order=self. sell(exectype=bt .Order .Limit, price=self . dataclose[0]*0.995, valid=self . datas[0]. datetime .date(0) + datetime . timedelta(days=1))
        self .log('SELL CREATE, %.2f' % self. dataclose[0])
import sys
if __name__ == '__main_' :
  args=sys .argv
  if len(args)<2:
    print("Usage: python %s model-type" % args[0])
    quit()
  print("begin training...")
  model=train(args[1])
  print("begin backtesting...")
# create a cerebro entity
  cerebro = bt .Cerebro()
# Add a strategy
  cerebro.addstrategy(MLPredictStrategy, model=model, print_log=False)
  data=bt.feeds . GenericCSVData(
    nullvalue=0.0,
    dataname=' ../../data/if-future-5min-test.csv',
    datetime=0,
    time=1,
    open=3,
    high=4,
    low=5,
    close=6,
    volume=7,
    dtformat=( '%Y-%m-%d'),
    tmformat=( ' %H:%M'),
  )
#添加数据
cerebro. adddata(data)
#设置处置资金
cerebro . broker. setcash(500000.0)
#设置佣金
cerebro. broker . setcommission(commission=30.0, margin=152000.0, mult=300.0, name=None)
cerebro . addsizer(bt . sizers.FixedSize, stake=1)
# Print out the starting conditions
print('initial value: %.2f' % cerebro. broker . getvalue())
# Run over everything
cerebro . run()
# Print out the final result
print('final value: %.2f' % cerebro . broker. getvalue())
#绘制图形
# cerebro.plot()
