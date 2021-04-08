# coding: utf-8

'''
参考说明 ： https://www.imooc.com/video/17910
           https://github.com/twfb/keras-imooc  对应的代码
运行：
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)
  python F:/develope/python/study_python/deep_learning/boston_housing_keras.py

'''

from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import numpy as np

# 获取训练数据、测试数据
(train_data, train_target), (test_data, test_target) = boston_housing.load_data()
print(train_data.shape)
print(test_data.shape)

print(train_target)
#print(test_target)

# 标准化 Xt = (X-mean)/std
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)

train_data = (train_data-mean)/std
test_data = (test_data-mean)/std

def build_model():
    model = Sequential()
    model.add(Dense(64, input_shape=(13,), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer=RMSprop(), loss='mse', metrics=['mae'])
    return model

# 交叉检验进行评分
k = 4
num_val_samples = len(train_data)//k
num_epoches = 100
all_scores=[]

for i in range(k):
    val_data = train_data[i*num_val_samples:(i+1)*num_val_samples]
    val_target = train_target[i*num_val_samples:(i+1)*num_val_samples]
    partial_train_data = np.concatenate(
        [train_data[:i*num_val_samples],
        train_data[(i+1)*num_val_samples:]],
        axis=0
    )
    partial_train_targets = np.concatenate(
        [train_target[:i*num_val_samples],
        train_target[(i+1)*num_val_samples:]],
        axis=0
    )
    model = build_model()
    model.fit(partial_train_data, partial_train_targets,epochs=num_epoches,batch_size=1,verbose=0)
    val_mse, val_mae = model.evaluate(val_data, val_target, verbose=0)
    all_scores.append(val_mae)
    print('第',i+1,'折, MSE:', val_mse, 'MAE：', val_mae)

print(np.mean(all_scores))

# 全量数据
model = build_model()
model.fit(train_data, train_target,epochs=80,batch_size=16,verbose=0)

test_mse,test_mae = model.evaluate(test_data, test_target)
