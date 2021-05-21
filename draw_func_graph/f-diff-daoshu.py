# -*- coding: utf-8 -*-

'''
python3.7   （python2.7报错）
    带箭头x-y坐标轴 , 参考： https://www.jianshu.com/p/af8a448d4d4f

运行： 函数求导数
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)
  conda install -y sympy

  python F:/develope/python/study_python/draw_func_graph/f-diff-daoshu.py -f "2*x**2"

'''

from sympy import *  #导入sympy库
import numpy as np  #导入numpy库
import argparse
import math

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='x**2/2', help='draw y=x**2/2')

    args = parser.parse_args()
    yfunc = args.f

    x = symbols('x')
    f_diff = diff(yfunc)    # 函数的导数
    print(f_diff)

if __name__ == '__main__':
    run()
