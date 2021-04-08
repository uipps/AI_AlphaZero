# coding: utf-8

'''
《零基础学机器学习》
参考说明 ： F:\develope\python\books\零基础学机器学习_sn54599\第1课 机器学习实战\练习用例 波士顿房价预测\代码\C01-3 Boston Housing Price.ipynb

使用keras中的数据集，并使用了sklearn中的线性回归模型

运行：
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)
  python F:/develope/python/study_python/deep_learning/boston_housing2_keras_sklearn.py

'''
import numpy as np # 导入NumPy数学工具箱
#import pandas as pd # 导入Pandas数据处理工具箱
from keras.datasets import boston_housing #从Keras中导入Boston Housing数据集
from sklearn.linear_model import LinearRegression #导入线性回归算法模型

#读入训练集和测试集
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

print ("数据集张量形状：", X_train.shape) #shape方法显示张量的形状
print ("第一个数据样本：\n", X_train[0]) #注意Python的索引是从0开始的

print ("第一个数据样本的标签：", y_train[0])


model = LinearRegression() #使用线性回归算法
model.fit(X_train, y_train) #用训练集数据，训练机器，拟合函数，确定参数

y_pred = model.predict(X_test) #预测测试集的Y值
print ('房价的真值(测试集)',y_test)
print ('预测的房价(测试集)',y_pred)

print("给预测评分：", model.score(X_test, y_test)) #评估预测结果
