# -*- coding: utf-8 -*-
'''
python2.7 可以

运行：
  python F:/develope/python/study_python/draw_func_graph/2x.py -f 2x-1

'''

import argparse 
import numpy as np
import math
import matplotlib.pyplot as plt


def f1(x):
    y=2*x
    return y
def f2(x):
    y=1/(x*x+1)
    return y
def f3(x):
    y=math.sin(x)/(math.exp(x)+1)


def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='2x', help='draw y=2x')
    #parser.add_argument('-f', dest='y=f(x), function ', action='store',nargs='?', default='2x', type=str, required=False, help='draw y=2x')
    
    args = parser.parse_args()
    func = args.f
    #print(func)

    ''' 画函数图 '''
    plt.figure(1)
    x=[]
    y=[]
    a=np.linspace(0,10,100)

    for i in a:
        x.append(i)
        y.append(f1(i))
    plt.plot(x,y)
    plt.show()



if __name__ == '__main__':
    run()
