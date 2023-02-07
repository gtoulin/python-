# 低购买策略
import datetime  # For dateti me objects
import backtrader as bt
#新建一个策略
class ThreeLowBuyStrategy (bt. Strategy):
  def log(se1f, txt, dt=None):
  dt = dt or self. datas[0]. datetime. date(0)
print('%s,%s' % (dt. isoformat(), txt))


def __init__(se1f):
    # 保存收盘价
  self. dataclose = se1f. datas[0]. close


def next(se1f):

    # 打印收盘价
  se1f.log('C1ose, %.2f' % sel1f. datac1ose[0])
  if self. dataclose[0] < se1f. dataclose[-1]:
    # 当前的收盘价低于昨天的收盘价
    if self. dataclose[-1] < self. dataclose[-2]:
    # .昨天的收盘价低于前天的收盘价
    # 买
      self.log('BUY CREATE, %2f' % se1f. datac1ose[0])
      self.buy()
