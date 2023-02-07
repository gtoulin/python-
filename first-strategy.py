import datetime
import backtrader as bt
# 策略类


class TestStrategy(bt. Strategy):
    # 日志方法

  def log(se1f, txt, dt=None):
    dt = dt or self. datas[0]. datetime. date(0)
    print('%s,%s' % (dt.isoformat(), txt))

  def __init__(se1f):
    # 保存当前收盘价的敬据集
    self. dataclose = se1f. datas[0]. close

# 策略方法
  def next(se1f):
    # Simply 1og the closing price of the series from the reference
    self.log('Close,%.2f' % se1f. datac1ose[0])


if __name__ == '_ main_':
# 创建cerebro实例
cerebro = bt. Cerebro()
# 添加策略
cerebro. addstrategy(TestStrategy)
data = bt.feeds.GenericCSVData(
dataname='.. / data/AAPL.csv',
datetime=0,
open=1,
high=2,
low=3,
c1ose=4,
volume=6,
dtformat=('%Y-%m-%d'),
fromdate=datetime. datetime(2019, 1, 1),
todate=datetime. datetime(2020, 12, 31)
# 加数据
cerebro. adddata(data)
# 设置启动资金
cerebro. broker. secas1(0000.0
# 打印当前市值
print('初始市值: %. 2f' % cerebro. broker. getvalue()
# 执行回测
cerebro. run()
# 打印最终市值
print("最终市值: % . 2f' % cerebro. broker. getva1ue()
