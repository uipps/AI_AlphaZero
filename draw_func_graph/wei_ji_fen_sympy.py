# -*- coding: utf-8 -*-
'''
python3.7


运行：
-- macbook下,conda python37
  conda activate ailearn_py37
  python ~/develope/python/study_python/draw_func_graph/wei_ji_fen_sympy.py

-- win10-conda-python3.7
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                 ( python3.7环境下)
  python F:/develope/python/study_python/draw_func_graph/wei_ji_fen_sympy.py



'''

import argparse
import sympy as sp
from sympy import cos,sin


def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='2*x', help='draw y=2x')
    #parser.add_argument('-f', dest='y=f(x), function ', action='store',nargs='?', default='2x', type=str, required=False, help='draw y=2x')
    parser.add_argument('-b', type=float, help='xrange, begin, default -2')
    parser.add_argument('-x', type=float, default=2, help='xrange, end, default 2')
    parser.add_argument('-y', type=float, default=2, help='y-Range, begin and end, default 2')
    parser.add_argument('--y_min', type=float, help='y-Range-min, begin, default -2')
    parser.add_argument('-s', type=float, default=0.01, help='x-step, end, default 0.1')

    args = parser.parse_args()
    yfunc = args.f
    xBegin = args.b
    xEnd = args.x         # x-range , max
    yMax = args.y
    yMin = args.y_min
    xStep = args.s
    #print(yfunc)
    if None==xBegin:
        xBegin = -1 * xEnd	# 默认对称，取x的反
    if None==yMin:
        yMin = -1 * yMax

    x = sp.Symbol('x')
    #print(x)

    # 原函数
    y1 = 3*x
    y2 = 3*x**3 + 2*x**2 + 1
    y3 = 1/x
    y4 = 3*x**2+2
    y5 = (1+1/x)**x
    #y6 = sp.sin(x)/x
    y6 = sin(x)/x

    # 1. 求导数
    print('\r\n\r\n ##### 求导数 #####')
    f1 = sp.diff(y1)
    print('\r\n原函数 y1 = {}' . format(y1))
    print('其导数 f1 = {}' . format(f1))

    f2 = sp.diff(y2)
    print('\r\n原函数 y2 = {}' . format(y2))
    print('其导数 f2 = {}' . format(f2))

    f3 = sp.diff(y3)
    print('\r\n原函数 y3 = {}' . format(y3))
    print('其导数 f3 = {}' . format(f3))

    f4 = sp.diff(y4)
    print('\r\n原函数 y4 = {}' . format(y4))
    print('其导数 f4 = {}' . format(f4))

    f5 = sp.diff(y5)
    print('\r\n原函数 y5 = {}' . format(y5))
    print('其导数 f5 = {}' . format(f5))

    f6 = sp.diff(y6)
    print('\r\n原函数 y6 = {}' . format(y6))
    print('其导数 f6 = {}' . format(f6))

    print('\r\n')

    # 2. 求积分
    print('\r\n\r\n ##### 求积分 #####')
    F1 = sp.integrate(f1, x)
    print('\r\n原函数 f1 = {}' . format(f1))
    print('其积分 F1 = {}' . format(F1))

    F2 = sp.integrate(f2, x)
    print('\r\n原函数 f2 = {}' . format(f2))
    print('其积分 F2 = {}' . format(F2))

    F3 = sp.integrate(f3, x)
    print('\r\n原函数 f3 = {}' . format(f3))
    print('其积分 F3 = {}' . format(F3))

    F4 = sp.integrate(f4, x)
    print('\r\n原函数 f4 = {}' . format(f4))
    print('其积分 F4 = {}' . format(F4))

    F5 = sp.integrate(f5, x)
    print('\r\n原函数 f5 = {}' . format(f5))
    print('其积分 F5 = {}' . format(F5))

    F6 = sp.integrate(f6, x)
    print('\r\n原函数 f6 = {}' . format(f6))
    print('其积分 F6 = {}' . format(F6))


    # 3. 求极限
    L1 = sp.limit(y1, x, 0)
    L2 = sp.limit(y2, x, 0)
    L3 = sp.limit(y3, x, 0)
    L4 = sp.limit(y4, x, 0)
    L5 = sp.limit(y5, x, 'oo')  # x->无穷大的时候, 需要用引号
    L6 = sp.limit(y6, x, 0)
    print('\r\n\r\n ##### 求极限 #####')
    print('\r\n原函数 y1 = {}' . format(y1))
    print('其极限 L1 = {}  (x->0)' . format(L1))
    print('\r\n原函数 y2 = {}' . format(y2))
    print('其极限 L2 = {}  (x->0)' . format(L2))
    print('\r\n原函数 y3 = {}' . format(y3))
    print('其极限 L3 = {}  (x->0)' . format(L3))

    print('\r\n原函数 y4 = {}' . format(y4))
    print('其极限 L4 = {}  (x->0)' . format(L4))

    print('\r\n原函数 y5 = {}' . format(y5))
    print('其极限 L5 = {}  (x->oo)' . format(L5))

    print('\r\n原函数 y6 = {}' . format(y6))
    print('其极限 L6 = {}  (x->oo)' . format(L6))


if __name__ == '__main__':
    run()
