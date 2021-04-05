# -*- coding: utf-8 -*-

'''
python3.7   （python2.7报错）
    带箭头x-y坐标轴 , 参考： https://matplotlib.org/2.0.2/examples/pylab_examples/ellipse_demo.html

运行：
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)

  python F:/develope/python/study_python/draw_func_graph/circle_ellipse.py -f "x**2/4+y**2" -z 9 -x 6 -y 3

  -- 需要修改一下代码
  python F:/develope/python/study_python/draw_func_graph/circle_ellipse.py -f "x**2/2+y**2-9" -x 5

'''

import matplotlib.pyplot as plt  #导入matplotlib库
import numpy.random as rnd
from matplotlib.patches import Ellipse
import argparse
import numpy as np
import turtle

NUM = 250

def graph_many_ellipse():
    ''' 多个椭圆和圆形 '''
    ells = [Ellipse(xy=rnd.rand(2)*10, width=rnd.rand(), height=rnd.rand(), angle=rnd.rand()*360)
        for i in range(NUM)]
    fig = plt.figure(0)
    ax = fig.add_subplot(111, aspect='equal')
    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(rnd.rand())
        e.set_facecolor(rnd.rand(3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.show()

def circle1():
    x = y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x,y)
    plt.contour(x, y, x**2 + y**2, [9])     #x**2 + y**2 = 9 的圆形
    plt.axis('scaled')
    plt.show()

def ellipse1():
    return 0
    #x*x /1 + y*y/4 = 2
    #绘制图形
    #plt.plot(x,y, c='b')
    #plt.show()

def draw_circle1():
    pen = turtle.Turtle()  #定义画笔实例
    a = 1                         #前进的长度
    for i in range(120):
        pen.lt(3)                #向左转3度
        pen.fd(a)               #向前走a的步长
    print(pen)
    turtle.mainloop()

def draw_ellipse1():
    pen=turtle.Turtle()                #定义画笔实例
    a=1
    for i in range(120):                
        if 0<=i<30 or 60<=i<90:        #控制a的变化
            a=a+0.2
            pen.lt(3)                  #向左转3度
            pen.fd(a)                  #向前走a的步长
        else:
            a=a-0.2
            pen.lt(3)
            pen.fd(a)
    print(pen)
    turtle.mainloop()

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='2*x', help='draw y=2x')
    parser.add_argument('-b', type=float, help='xrange, begin, default -2')
    parser.add_argument('-x', type=float, default=4, help='xrange, end, default 2')
    parser.add_argument('-y', type=float, default=4, help='y-Range, end, default 2')
    parser.add_argument('--y_min', type=float, help='y-Range-min, begin, default -2')
    parser.add_argument('-s', type=float, default=0.01, help='x-step, end, default 0.1')
    parser.add_argument('-z', type=float, default=9, help='z-value')

    args = parser.parse_args()
    func = args.f
    xBegin = args.b
    xEnd = args.x         # x-range , max
    yMax = args.y
    yMin = args.y_min
    xStep = args.s
    zVal = args.z
    if None==xBegin:
        xBegin = -1 * xEnd
    if None==yMin:
        yMin = -1 * yMax

    #graph_many_ellipse()   # 多个椭圆和圆形
    #ellipse1()             # 椭圆
    #circle1()               # 圆
    #draw_circle1()     # 动画画椭圆
    #draw_ellipse1()   # 动画画椭圆

    x = np.arange(xBegin, xEnd, xStep)
    y = np.arange(yMin, yMax, xStep)
    x, y = np.meshgrid(x,y)
    plt.contour(x, y, eval(func), [zVal])       # -f "x**2/4+y**2" -z 9 的椭圆形
    #plt.contour(x, y, eval(func), 0)                # -f "x**2/4+y**2-9"
    #plt.axis('scaled')
    plt.show()


if __name__ == '__main__':
    #graph_many_ellipse()
    run()
