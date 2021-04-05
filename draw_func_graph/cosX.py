# -*- coding: utf-8 -*-

'''
python2.7 可以

    参考： https://blog.csdn.net/qq_46672746/article/details/109498411

运行：
  python F:/develope/python/study_python/draw_func_graph/cosX.py

'''

import matplotlib.pyplot as plt
import numpy as np


# 画 y = cos(x) 图像
x=np.linspace(-3,3,256,endpoint=80) #图像横坐标范围
#plt.xlim(-3*np.pi,3*np.pi) #坐标轴横坐标取值范围

y=1/3*x*x*x - x  # y = 1/3*x^3 - x

plt.plot(x,y,color='red',linewidth=5,linestyle='-') #根据x y 数组绘制直线曲线
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
