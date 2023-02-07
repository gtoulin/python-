import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
#绘图函数
def draw_err (delt):
  plt . figure(figsize=(15, 8))
  plt . plot(delt, color= 'r' ,markersize=1, linestyle='-', labe1="real")
  plt. grid(True)
  plt . legend()
  plt. show( )
dataset = pd.read_csv(" ../data/stock-predict.csv")
data_num=dataset . shape[0]
train_num=int(0.8*data_num)
test_num=int (0.2*data_num)
print("train_ num:", train_num, "test_ num", test_num)
x_train = dataset. iloc[ :train_num-1,1:-2].values #开高低收量共5个特征
y_train = dataset . iloc[ :train_num-1, -2].values #预测高点
x_test = dataset.iloc[train_num:-2,1: -2]. values
y_test = dataset. iloc[train_num:-2,-2].values #测试集的高点
#使用感知器回归
from sklearn . preprocessing import StandardScaler
scaler = StandardScaler() 
scaler. fit(X_train)
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)
#线性回归
from sklearn. linear_model import LinearRegression
lr = LinearRegression()
lr=lr . fit(X_train, y_train)
r_pred=lr . predict(X_test)
lr_delt=lr_pred-y_test 
lr_mae=np . mean(np . abs(lr_delt))
print("线性回归预测平均绝对误差: ",lr_mae)
# draw_ err(1r_ delt)
#多项式回归
from sklearn. preprocessing import PolynomialFeatures
from sklearn. linear_model import LinearRegression
from sklearn. pipeline import Pipeline
poly_model=Pipeline([( 'poly', PolynomialFeatures ( degree=1)),('linear', LinearRegression(fit_intercept=False))])
poly_model
poly_model. fit(X_train, y_train)
poly_pred=poly_model . predict(X_test)
poly_de1t=poly_pred-y_test
poly_mae=np . mean(np . abs(poly_delt))
print( "3次多项式回归平均预测绝对误差: ", poly_mae)
#线性脊回归
from sklearn. linear_model import Ridge 
ridge=Ridge(alpha=100.0)
ridge=ridge. fit(X_train, y_train)
ridge_pred=ridge . predict(X_test)
ridge_delt=ridge_pred-y. test
ridge_mae=np . mean(np . abs (ridge_delt))
print("脊回归预测平均绝对误差:",ridge_mae)
#决策树回归
from sklearn import tree
tree_model = tree . DecisionTreeRegressor()
tree_model = tree_model. fit(X_train, y_train)
tree_pred=tree_model. predict(X_test)
tree_delt=tree_pred-y_test
tree_mae=np . mean(np . abs(tree_delt))
print("决策树回归预测平均预测绝对误差: ", tree_mae)
#支撑向量机回归
from sklearn import svm
svr = svm.SVR()
svr=svr. fit(X_train, y_train)
svr_pred=svr . predict(X_test)
svr_delt=svr_pred-y_test
svr_mae=np.mean(np . abs(svr_delt))
print("支撑向量机回归预测平均绝对误差:",svr_mae)
# draw_ err(svr_ delt)
#随机森林回归
from sklearn. ensemble import RandomForestRegressor
rf=RandomForestRegressor()
rf=rf.fit(X_train, y_train)
rf_pred=rf . predict(X_test )
rf_delt=rf_pred-y_test 
rf_mae=np . mean(np. abs(rf_delt))
print("随机森林回归预测平均绝对误差: ",rf_mae)
# draw_ err(rf_ delt)
#最近邻回归
from sklearn. neighbors import KNeighborsRegressor
knr = KNeighborsRegressor (n_neighbors=6 )
knr=knr . fit(X_train, y_train)
knr_pred=knr . predict(X_test )
knr_delt=knr_pred-y_test
knr_mae=np . mean(np . abs(knr_delt))
print("最近邻回归预测平均绝对误差:",knr_mae)
# draw_ err(knr_ delt)
#使用感知器回归
from sklearn. neural_network import MLPRegressor
mlp=MLPRegressor (hidden_layer_sizes=(6,18,6), activation= 'logistic',max_iter=150000)
m1p=mlp. fit(X_train, y_train)
m1p_pred=mlp. predict(X_test)
m1p_delt=mlp_pred-y_test
m1p_mae=np . mean(np . abs(mlp_delt))
print("感知器神经网络预测平均绝对误差:", m1p_mae)
draw_err(m1p_delt)
#高斯过程回归
from sklearn. gaussian_process import GaussianProcessRegressor
from sklearn. gaussian_process . kernels import DotProduct, WhiteKernel
kernel = DotProduct()
# kernel = DotProduct() + WhiteKernel( )
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0)
gpr-gpr. fit(X_train, y_train)
gpr_pred=gpr . predict(X_test)
gpr_delt=gpr.pred-y_test
gpr_mae=np . mean(np . abs(gpr_delt))
print("高斯过程回归预测平均绝对误差: ",gpr. mae)
draw_err(gpr_delt)
