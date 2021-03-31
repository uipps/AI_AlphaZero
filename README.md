# AI_AlphaZero
人工智能，深度学习，基于AlphaZero的算法，实现五子棋、中国象棋、围棋等的自学习，还将尝试用AlphaZero实现青蛙过河、野人过河、走迷宫、两人取火柴游戏等...... 不同分支代表不同游戏，例如gomoku，gobang就是五子棋，chess_chinese ( Chinese chess ) 等

本文参考了郭宪所著《深入浅出强化学习编程实战》的代码，SN：9-787121-36746-5 .在此表示感谢！

# 人机对战
```
python human_play.py  
```

输入格式是： 2,3
表示的意义自己看一下就知道了

## 修改人机对战人先下
参数中加


## 修改棋盘大小


# 获取训练模型
```
python train.py
```

## 修改默认库
默认用的pytorch， 修改train.py文件，将
```
#from policy_value_net import PolicyValueNet  # Theano and Lasagne
from policy_value_net_pytorch import PolicyValueNet  # Pytorch
#from policy_value_net_tensorflow import PolicyValueNet # Tensorflow
#from policy_value_net_keras import PolicyValueNet # Keras
```
其他加上注释，只留一个即可，每行后面有注释用的哪个库

