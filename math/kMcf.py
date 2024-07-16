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

  python F:/develope/python/study_python/math/kMcf.py -l 120 -d 6924570972517795787222999651 -m 56 

  # -d 是否用引号都可以
  python F:/develope/python/study_python/math/kMcf.py -l 120 -m 56 -d "6924570972517795787222999651.1" 
  python F:/develope/python/study_python/math/kMcf.py -l 120 -m 56 -f mpmath -d "6924570972517795787222999651.1" 

  python F:/develope/python/study_python/math/kMcf.py -l 120 -m 56 -f gmpy2 -d "6924570972517795787222999651.1"    # 小数点后只有37位, 不推荐

'''

#from sympy import *  #导入sympy库
#import numpy as np  #导入numpy库
import argparse
#import sys
#import math
from mpmath import mp
from decimal import Decimal, getcontext 
import gmpy2

# gmpy2 计算结果小数点后只有37位
def nth_root_gmpy2(num, n, precision=200): 
    gmpy2.get_context().precision=precision
    num = gmpy2.mpfr(num)
    return gmpy2.root(num, n)

"""  
    计算一个非常大的数的n次方根，并保留precision位小数。  
    :param number: 字符串，表示要计算的大数，可以包括小数。  
    :param n: 正整数，表示次方根的次数。  
    :param precision: 整数，表示结果要保留的小数位数。  
    :return: Decimal对象，表示计算结果。  
"""  
def calculate_nth_root(num, n,  precision=200):      
    getcontext().prec = precision + 10  # 额外增加一些精度以避免舍入误差  
    return Decimal(num) ** (Decimal(1) / Decimal(n))

# num可以是308位以内的float。不能是string类型的，否则报错：TypeError: cannot create mpf from 
def high_precision_nth_root(num, n):
    return mp.root(num, n)

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    # print(sys.float_info) # float类型，支持的最大、最小值 max=1.7976931348623157e+308, min=2.2250738585072014e-308
    parser.add_argument('-d', type=float, default=2.0, help='m√d, the d, default 2.0')
    parser.add_argument('-s', type=str, default="", help='m√d, the d, default 2.0')    # 底数是字符串类型，超长字符串
    parser.add_argument('-m', type=int, default=20, help='m√d,  the m , default 20')
    parser.add_argument('-l', type=int, default=100, help='scale, the num length behind dot., default 100')
    parser.add_argument('-f', type=str, default="", help='function ,  default NULL ')      # 指定处理的func

    args = parser.parse_args()
    dishu = args.d
    dishu_str = args.s
    kaifangci = args.m
    rlt_len = args.l
    l_func = args.f

    # 见文档 https://mpmath.org/doc/current/functions/powers.html?highlight=root#mpmath.root
    # -d 可以是负数，开偶数次方的时候不能是负数。
    if dishu < 0 or ('-' in dishu_str):
        print(" 参数-d,底数虽然可以为负数，简单起见，本简单代码暂不支持负数! ") 
        return 0
    if rlt_len < 0 :
        print(" 参数-l,小数点后位数不能是负数 ") 
        return 0
    if kaifangci < 0 : 
        # 文档中可以取0，结果都是1 ， （虽然似乎无意义z^(1/n)）
        print(" 参数-m, 必须是不小于0的正整数 ") 
        return 0

    if '' == dishu_str:
        dishu_str = str(dishu)

    if ('mpmath' == l_func):
        mp.dps = rlt_len  # 设置保留小数点后 100 位小数
        result_root = high_precision_nth_root(dishu, kaifangci) # 只能是float类型，不能是string类型，否则报错
    elif 'gmpy2' == l_func :
        result_root = nth_root_gmpy2(dishu_str, kaifangci, rlt_len)  # 小数点后只有37位
    else :
        # 整数部分超过308位都能处理
        result_root = calculate_nth_root(dishu_str, kaifangci, rlt_len)
    #print("2 的 30 次方根（精确到 100 位）：", result_root)
    print(result_root)

if __name__ == '__main__':
    run()
