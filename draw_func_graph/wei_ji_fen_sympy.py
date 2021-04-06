# -*- coding: utf-8 -*-
'''
python3.7


运行：
-- macbook下,conda python37
  conda activate ailearn_py37
  python ~/develope/python/study_python/draw_func_graph/wei_ji_fen_sympy.py -f "3*x" -e 1

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
    #parser.add_argument('-f', dest='y=f(x), function ', action='store',nargs='?', default='2*x', type=str, required=False, help='draw y=2x')
    parser.add_argument('-e', type=int, help='print example ? 0-no, 1-yes')
    ''' 解析参数 '''
    args = parser.parse_args()
    yfunc = args.f
    isexample = args.e

    print('对函数求导数、求积分、求极限：')
    #example01()
    dao_jifen_jixian(yfunc)
    if isexample:
        for y_fun in getExampleFunc():
            if y_fun == '(1+1/x)**x':
                dao_jifen_jixian(y_fun, 'oo')
            else :
                dao_jifen_jixian(y_fun, 0)

def dao_jifen_jixian(yfunc, xLimit=0):
    x = sp.Symbol('x')

    # 原函数
    #y1 = 3*x
    y1 = eval(yfunc)
    print('  ##### 原函数 y = {} #####' . format(y1))

    # 1. 求导数
    #print('\r\n\r\n ##### 求导数 #####')
    f1 = sp.diff(y1)
    print('  其导数 f\'(x) = {}' . format(f1))

    # 2. 求积分
    #print('\r\n\r\n ##### 求积分 #####')
    F1 = sp.integrate(y1, x)
    print('  其积分 F(x) = {}' . format(F1))

    # 3. 求极限
    #print('\r\n\r\n ##### 求极限 #####')
    L1 = sp.limit(y1, x, xLimit)
    print('  其极限 lim(y) (x->{}) = {}  ' . format(xLimit, L1))
    # 换行
    print()

def getExampleFunc():
    y1 = '3*x'
    y2 = '3*x**3 + 2*x**2 + 1'
    y3 = '1/x'
    y4 = '3*x**2+2'
    y5 = '(1+1/x)**x'
    #y6 = sp.sin(x)/x
    y6 = 'sin(x)/x'
    return [y1, y2, y3, y4, y5, y6]

if __name__ == '__main__':
    run()
