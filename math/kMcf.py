# -*- coding: utf-8 -*-

'''
python3.7    

运行：  
  C:/ProgramData/Anaconda3/condabin/conda activate py307                                ( python3.7环境下)
  conda install -y sympy

  参数说明：
    -d  √n, 就是开方底数n，默认2
    -m  任意实数n的m次方根，这里m必须是大于1的正整数，
    -l    计算精度，结果保留多少小数点位数，默认100

  python F:/develope/python/study_python/math/kMcf.py -l 120 -d 2 -m 30 

'''

#from sympy import *  #导入sympy库
#import numpy as np  #导入numpy库
import argparse
#import math
from mpmath import mp

def high_precision_nth_root(num, n):
    return mp.root(num, n)

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=float, default=2.0, help='m√d, the d, default 2.0')
    parser.add_argument('-m', type=int, default=20, help='m√d,  the m , default 20')
    parser.add_argument('-l', type=int, default=100, help='scale, the num length behind dot., default 100')

    args = parser.parse_args()
    dishu = args.d
    kaifangci = args.m
    rlt_len = args.l

    # 见文档 https://mpmath.org/doc/current/functions/powers.html?highlight=root#mpmath.root
    # -d 可以是负数，开偶数次方的时候不能是负数。
    if dishu < 0 :
        print(" 参数-d,底数虽然可以为负数，简单起见，本简单代码暂不支持负数! ") 
        return 0
    if rlt_len < 0 :
        print(" 参数-l,小数点后位数不能是负数 ") 
        return 0
    if kaifangci < 0 : 
        # 文档中可以取0，结果都是1 ， （虽然似乎无意义z^(1/n)）
        print(" 参数-m, 必须是不小于0的正整数 ") 
        return 0

    mp.dps = rlt_len  # 设置保留小数点后 100 位小数
    result_root = high_precision_nth_root(dishu, kaifangci)
    #print("2 的 30 次方根（精确到 100 位）：", result_root)
    print(result_root)

if __name__ == '__main__':
    run()
