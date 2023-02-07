import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn . neighbors import KNeighborsClassifier
from sklearn . naive_bayes import GaussianNB
from sklearn. ensemble import RandomForestClassifier
from sklearn . multiclass import OneVsRestclassifier
from sklearn. svm import LinearSVc
from sklearn. svm import SVC
from sklearn import gaussianprocess
from sklearn. neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn. ensemble import AdaBoostClassifier
from sklearn . multioutput import MultioutputClassifier
from xgboost import XGBClassifier
#绘图函数
def draw_err(delt):
  plt . figure(figsize=(15, 8))
  plt . plot(delt, color= 'r ',markersize=1, linestyle='-', labe1="delt")
  plt. grid(True)
  plt . legend()
  plt. show()
# usage of xgboost
# setup: pip install xgboost
# from xgboost import XGBClassifier
# model=XGBCliassifer()
# https://scikit-learn .org/stable/ auto examples/classification/plot_ classifier_ comparison . html
# name 训练的模型 名称:
# tree--决策树分类器
def train(name, filename=" ../ ../data/if- future- 5min- label-training .csv"):
#使用10日数据判断当前的分类(买，卖，持有)
  training_dataset = pd . readcsv(filename)
  training_data_num=training_dataset . shape[ 0]
  print("training data_ num:", training_datanum)
  x_train = training_dataset . iloc[:,3:].values #训练集开高低收量5*10=50个特征
  y_train = training_dataset . iloc[ :,2].values #训练集的分类识别号(1, -1, 0)

  model=None
  if name=='tree' :
    model-tree .DecisionTreeClassifier()
  elif name== 'knn' :
    model = KNeighborsClassifier(n_neighbors=3)
  elif name=='rf' :
    model = RandomForestclassifier(n_estimators=3, random_state=1)
  elif name==' sVm' :
    model = SVC(kernel= ' linear', random_state=1, C=0.1)
  elif name== ' naive ' :
    model-GaussianNB( )
  elif name==' gauss':
    model=gaussian_process.GaussianProcessClassifier()
  elif name== ' mlp' :
    model = MLPClassifier(solver= 'sgd',activation= 'logistic', alpha=1e-4, hidden_layer_sizes=(5,3 ), random_state=1,
    max_iter=1000, verbose=True, learning_rate_init= .00001 )
  elif name== ' xgboost' :
    model=XGBClassifier()
  elif name== 'adaboost' :
    model=AdaBoostClassifier()
  if (model !=None):
    model = model.fit(x_train, y_train)
  return model

def test (model,filename="../ ../data/ if -future 5min-label -test .csv"):
  test_dataset=pd. read_csv(filename )
  test_data_num=test_dataset . shape[0]
  print("test_ data num:",test_data_num)
  x_test = test_dataset. iloc[:,3:].values #测试集开高低收量5*n个特征
  y_test = test_dataset. iloc[:,2].values #测试集标记

  test_pred=model. predict(x_test)
  test_mae=np .mean(np. abs(test_pred-y_test))
  print("预测平均绝对误差: " ,test_mae)
  draw_err(test_pred)

import sys
if __name__ =='__main__':
  args=sys .argv
  if len( args)<2:
    print( "usage: python %s model-type" % args[0])
    quit()
  model=train( args[1])
  test(model)


