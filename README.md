# 这是中国象棋，python3版本
  暂不支持python2，本程序在python3.7下运行通过。 具备基本棋盘和走子功能，先从单机版对战开始，逐渐加入人工智能功能。参考github项目 chengstone/cchess-zero

## 运行方法
命令行下执行：
```
python main.py --mode play --ai_count 1 --ai_function mcts --play_playout 1200 --human_color w
```
### 下棋参数说明
 - --ai_count 指定ai的个数，1是人机对战，2是看两个ai下棋
 - --ai_function 指定ai的下棋方法，是思考（mcts，会慢），还是直觉（net，下棋快）
 - --play_playout 指定ai进行MCTS的模拟次数
 - --delay和--end_delay默认就好，两个ai下棋太快，就不知道俩ai怎么下的了：）
 - --human_color 指定人类棋手的颜色，w是先手，b是后手


## 也可自己训练
但是需要你的显卡、cpu够好哦，才能训练出AI高手，不然依然很烂，训练命令

```
python main.py --mode train --train_playout 1200 --batch_size 512 --search_threads 16 --processor gpu --num_gpus 2 --res_block_nums 7
```

### 训练参数说明
 - --mode 指定是训练（train）还是下棋（play），默认是训练
 - --train_playout 指定MCTS的模拟次数，论文中是1600，我做训练时使用1200
 - --batch_size 指定训练数据达到多少时开始训练，默认512
 - --search_threads 指定执行MCTS时的线程个数，默认16
 - --processor 指定是使用cpu还是gpu，默认是cpu
 - --num_gpus 指定gpu的个数，默认是1
 - --res_block_nums 指定残差块的层数，论文中是19或39层，我默认是7
