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
    #parser.add_argument('-d', type=str, default='x**2/2', help='draw y=x**2/2')
    parser.add_argument('-d', type=int, default=2, help='m√d, the d, default 2')
    parser.add_argument('-m', type=int, default=20, help='m√d,  the m , default 20')
    parser.add_argument('-l', type=int, default=100, help='scale, the num length behind dot., default 100')

    args = parser.parse_args()
    dishu = args.d
    kaifangci = args.m
    rlt_len = args.l

    if rlt_len < 0 or dishu < 0 or kaifangci < 0 :
        print(" error! ") 
        return 0

    mp.dps = rlt_len  # 设置保留小数点后 100 位小数
    result_root = high_precision_nth_root(dishu, kaifangci)
    #print("2 的 30 次方根（精确到 100 位）：", result_root)
    print(result_root)

if __name__ == '__main__':
    run()
