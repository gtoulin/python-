import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets 
from sklearn. model_selection import train_test_split
from sklearn. neighbors import KNeighborsC1assifier
iris=datasets.load_iris()
print (iris['DESCR' ])
print(iris[' data'])
X= iris. data[:,:2] #前两列
y=iris. target
print (y)
x_min=X[:, 0]. min()-0.5
x_max=X[:,0].max()+0.5
y_min=X[:, 1].min()-0.5
y_max=X[:, 1]. max()+0.5
plt. figure(2, figsize=(8, 6))
plt.clf()
plt.scatter(X[:,0],x[:,1], c=y, cmap=plt. cm. Set1, edgeco1ors="k")
plt. x1abe1 ("Sepa11ength")
plt. ylabe1 ("Sepal width")
plt. x1im(x_min, x_max)
plt. y1im(y_min, y_max)
plt.legend()
#划分训练集与测试集
X_train, X_test, y_train, y_test=train_test_split(
  iris['data'],iris['target'],test_size=0.25,random_state=0
)
print("X_train 大小: {}". format(X_train. shape))
print("y_ _train大小: 0". format (y_train. shape))
print("X_ _test大小: 0". format (X_test. shape))
print("y_ test大小: 0". format (y_test. shape))
knn=KNeighborsClassifier(n_neighbors=9)
#仅取后面两个特征，进行训练
knn. fit(X_train[:,:], y_train)
#预测测试
new_data-np. array([[7.7,3.1, 1.2,0.5]])
prediction = knn. predict(new_data[:, :])
print ("Prediction: 0". format (prediction))
print("Predicted target name: 0 ". format (iris[' target_ _names' ] [prediction]))
#测试校验
y_pred=knn. predict(X_test[:, :]) 
print("k最近邻分类器测试集预测: 0} ". format (y_pred))
print("测试集真值: 0". format(y_test))
print("k最近邻分类器预测得分: {:. 2f}". format(knn.score(X_test[:, :],y_test)))
plt. show()

from sklearn. tree import DeioinTreassifieri,ExtraTreeClassifier
decision_tree=DecisionTreeClassifier(max_depth=4)
decision_tree.fit(X_train[:, :], y_train)
#测试校验
y_decsion_tre_pred=decision_tree.predict(X_test[:,:])
print("决策树分类器测试集预测: {}".format(y_decision_tree_pred))
print("测试集真值0".format(y_test))
print("决策树分类器预测得分: {:.2f} ".format(decision_tree.score(X_test[:,:],y_test)))
extra_tree=ExtraTreeClassifier (max_depth=7)
extra_tree.fit(X_train[:, :],y_train)
#测试校验
y_extra_tree_pred=extra_tree.predict(X_test[:,:])
print("榭分类器测试集预测: {}". format(y_extra_tree_pred))
print("测试集真值: {}". format(y_test))
print("江树分关器预测得分: {:.2f}".format(extra_tree.score(X_test[:,:],y_test)))
from sklearn.svm import LinearSVC, MuSVC
linear_svc=LinearSVC()
linear_svc. fit(X_train[:, :], y_train)
#测试校验
y_linear_svc_pred=linear_svc. predict(X_test[:,:])
print("Lhnar5C分英器测试集预测: {}".format(y_linear_svc_pred))
print("测试集真值: {}". format(y._test))
nu_svc=NuSVC(kerne1='rbf')
nu_svc.fit(X_train[:, :], y_train)
#测试校验
y_nu_svC_pred=nu_svc.pedict(X_test[:,:])
print("IlusvC分类器测试集预测: {}". format(y_nu_svC_pred))
print("测试集真值: {}".format(y_test))
print("MuSvC分类器预测得分: {:.2f}". format(nu_svc.score(X_test[:,:], y_test)))

from sklearn import neural_network as nn
mlp=nn. MILPClassifier()
mlp.fit(X_train[:, :],y_train)
#测试校验
y_mlp_pred=mlp.predict(X_test[:,:])
print ("感知器神经网络分类器测试集预测: {}". format(y_mlp_pred))
print("测试集真值: {}". format(y_test))
print("感知器神经网络分类器预测得分: [:.2f]". format(mlp. score(X_test[:, :], y . test)))
from sklearn. neighbors import RadiusNeighborsC1assifier
rnn=RadiusNeighborsC1assifier()
rnn. fit(X_train[:, :],y_train)
#测试校验
y_rnn_pred=rnn. predict(X_test[:, :])
print ("Radi us最近邻分类器测试集预测: 0". format (y_rnn_pred))
print("测试集真值: 0". format(y_test))
print ("Radius最近邻分类器分类器预测得分: {:. 2f}". format (rnn. score(X_test[:, :],y_test)))
from sklearn. naive_bayes import GaussianNB
naive_bayes=GaussianNB ()
naive_bayes. fit(X_train[:, :], y_train) 
#测试校验
y_naive_bayes_pred=naive_bayes. predict(X_test[:, :])
print("朴素贝叶斯分类器测试集预测: {}". format (y_naive_bayes_pred))
print("测试集真值: 0". format (y_test))
print("朴素贝叶斯分类器分类器预测得分: {:. 2f}". format (naive_bayes.score(X_test[:, :],y_test)))
from sklearn.linear_model import RidgeClassifier
ridge_classifier=RidgeClassifier()
ridge_classifier. fit(X_train[:, :], y_train)
#测试校验
y_ridge_classifier_pred=ridge_classifier. predict(X_test[:, :])
print("脊回归分类器测试集预测: 0 ". format(y_ridge_classifier_pred))
print("测试集真值: 0". format(y_test))
print("脊回归分类器分类器预测得分: {:. 2f}". format(ridge_classifier.score(X_test[:,:],y_test)))

from sklearn. gaussian_process import GaussianProcessClassifier
gauss=GaussianProcessClassifier ()
gauss. fit(X_train[:, :], y_train)
#测试校验
y_gauss_pred=gauss. predict(X_test[:, :])
print("高斯过程分类器测试集预测: {} ". format(y_gauss_pred))
print("测试集真值: 0". format (y_test))
print("高斯过程分类器分类器预测得分: {:. 2f}".format(gauss. score(X_test[:, :],y_test)))
from sklearn. ensemble import GradientBoostingClassifier, RandomForestClassifier
gb=GradientBoostingClassifier()
gb. fit(X_train[:, :], y_train)
#测试校验
y_gauss_pred=gb. predict(X_test[:, :])
print ("梯度提升分类器测试集预测: 0". format(y_gauss_pred))
print("测试集真值: 0 ". format (y_test))
print("梯度提升分类器分类器预测得分: {:. 2f}". format(gb. score(X_test[:, :],y_test)))
rf=RandomForestClassifier()
rf. fit(X_train[:, :], y_train) 
#测试校验
y_rf_pred=rf. predict(X_test[:, :])
print("随机森林分类器测试集预测: {}". format(y_rf_pred))
print("测试集真值: 0". format(y_test))
print ("随机森林分类器分类器预测得分: {:.2f}". format (rf. score(X_test[:, :],y_test)))
