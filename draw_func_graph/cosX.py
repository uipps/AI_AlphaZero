# -*- coding: utf-8 -*-

'''
python2.7 可以

    参考： https://blog.csdn.net/qq_46672746/article/details/109498411

运行：（也可以用 f_withX_Y.py 程序 ）
  python F:/develope/python/study_python/draw_func_graph/cosX.py -f "np.cos(np.pi*x)" -x 2 -y 1.5
  python F:/develope/python/study_python/draw_func_graph/cosX.py -f "np.cos(x)" -x 2 -y 1.5 

  直接用
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py -f "np.cos(x)" -x 2 -y 1.5

'''

import matplotlib.pyplot as plt
import numpy as np
import argparse

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
if None==xBegin:
    xBegin = -1 * xEnd	# 默认对称，取x的反
if None==yMin:
    yMin = -1 * yMax

# 画 y = cos(x) 图像
#x=np.linspace(xBegin, xEnd, 256, endpoint=80) #图像横坐标范围
x=np.arange(xBegin, xEnd, xStep)
#plt.xlim(-3*np.pi,3*np.pi) #坐标轴横坐标取值范围
plt.ylim(yMin, yMax) 

#y=1/3*x*x*x - x  # y = 1/3*x^3 - x
#y=np.cos(2*np.pi*x)
#y=np.cos(np.pi*x/2)
#y=np.cos(np.pi*x)
y=eval(yfunc)

plt.plot(x,y,color='red',linewidth=1,linestyle='-') #根据x y 数组绘制直线曲线
plt.show()


'''
import math

# 一个图里面两个图像
x=np.linspace(-np.pi,np.pi,256,endpoint=80)
y1=np.cos(2*np.pi*x)			# y= cos(2pi*x)
y2=1/(math.e**x)*np.cos(2*np.pi*x)      # y=1/(e^x) * cos(2pi*x)

plt.plot(x,y1,label="y1=cos(2*pi*x)")
plt.plot(x,y2,label='(1/e**x)*cos(2*pi*x)')
plt.legend(loc=1)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
'''

'''
#  扇形图
plt.rcParams['font.sans-serif']=['SimHei']  #解决中文乱码

plt.figure(figsize=(6,9)) #调节图形大小
labels = [u'Dogs',u'Hogs',u'Frogs',u'Logs'] #定义标签
sizes = [45, 30, 15, 10] #每块值
colors = ['green', 'yellow', 'blue', 'red'] #每块颜色定义
explode = (0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend() # 右上角显示
plt.show()
'''
