# -*- coding: utf-8 -*-
'''
python3.7   （python2.7报错）
    带箭头x-y坐标轴 , 参考： https://www.jianshu.com/p/af8a448d4d4f

运行：
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "1/x" -y 5 -x 1
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "2*x" -y 5 -x 2

  -- 设定x,y的取值范围和步长s
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "1/3*x*x*x - x" -x 2 -y 1 -s 0.001

  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "np.cos(x)" -x 2 -y 1 -s 0.1

  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "np.cos(x)" -x 2 -y 1.5  
  
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "np.sqrt(x)" -b 0 -x 4 --y_min 0 -y 2 


  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "np.sin(x)/(np.exp(x)+1)" -x 2 -y 1.5 -s 0.1
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "1/(x*x+1)"

-- 可以保存图片，--save参数给出文件名(路径)即可
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "2**x" -x 7 -y 1.2 -s 0.01 --save "D:/temp/aaaa1"
'''

import matplotlib.pyplot as plt  #导入matplotlib库
import numpy as np  #导入numpy库
import mpl_toolkits.axisartist as axisartist
import argparse


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
    parser.add_argument('--save', type=str, help='save image')

    args = parser.parse_args()
    yfunc = args.f
    xBegin = args.b
    xEnd = args.x         # x-range , max
    yMax = args.y
    yMin = args.y_min
    xStep = args.s
    xSave = args.save
    #print(yfunc)
    if None==xBegin:
        xBegin = -1 * xEnd	# 默认对称，取x的反
    if None==yMin:
        yMin = -1 * yMax
    if None==xSave:
        xSave = 0

    ''' 画函数图 '''
    ## 1.创建画布并引入axisartist工具。
    #创建画布
    fig = plt.figure(figsize=(8, 8))
    #使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axisartist.Subplot(fig, 111)  
    #将绘图区对象添加到画布中
    fig.add_axes(ax)

    ## 2.绘制带箭头的x-y坐标轴
    #通过set_visible方法设置绘图区所有坐标轴隐藏
    ax.axis[:].set_visible(False)

    #ax.new_floating_axis代表添加新的坐标轴
    ax.axis["x"] = ax.new_floating_axis(0,0)
    #给x坐标轴加上箭头
    ax.axis["x"].set_axisline_style("->", size = 1.0)
    #添加y坐标轴，且加上箭头
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    #设置x、y轴上刻度显示方向
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")


    ## 3.在带箭头的x-y坐标轴背景下，绘制函数图像
    #生成x步长为0.1的列表数据
    x = np.arange(xBegin, xEnd, xStep)
    plt.xlim(xBegin, xEnd)        #设置x、y坐标轴的范围
    plt.ylim(yMin, yMax)

    #生成sigmiod形式的y数据
    #y=1/(1+np.exp(-x))
    #y=1/3*x*x*x - x  # y = 1/3*x^3 - x
    y=eval(yfunc)		# 字符串转表达式
    #y=1/x

    #绘制图形
    plt.plot(x,y, c='b')
    if xSave:
        l_file = xSave + '.png'
        plt.savefig(l_file)      #保存图片
        print('save image to ' + l_file)
    plt.show()

if __name__ == '__main__':
    run()
