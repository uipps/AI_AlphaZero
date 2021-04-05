# -*- coding: utf-8 -*-
'''
python3.7   （python2.7报错）
    带箭头x-y坐标轴 , 参考： https://www.jianshu.com/p/af8a448d4d4f

运行：
  python F:/develope/python/study_python/draw_func_graph/f_withX_Y.py

'''

import matplotlib.pyplot as plt  #导入matplotlib库
import numpy as np  #导入numpy库
import mpl_toolkits.axisartist as axisartist

'''
# 画 y = cos(x) 图像
x=np.linspace(-3*np.pi,3*np.pi,256,endpoint=80) #图像横坐标范围
y=np.cos(x)  # y = cos(x)
plt.plot(x,y,color='red',linewidth=5,linestyle='-') #根据x y 数组绘制直线曲线
plt.show()
'''

'''
#没有x，y坐标轴的情况

#生成x步长为0.1的列表数据
x = np.arange(-15,15,0.1)
#plt.xlim(-12,12)		#设置x、y坐标轴的范围
#plt.ylim(-1, 1)

#生成 sigmiod 形式的y数据
y=1/(1+np.exp(-x))

#绘制图形
plt.plot(x,y, c='b')
plt.show()
'''


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
x = np.arange(-2,2,0.01)
#plt.xlim(-12,12)		#设置x、y坐标轴的范围
#plt.ylim(-1, 1)	

#生成sigmiod形式的y数据
#y=1/(1+np.exp(-x))
y=1/3*x*x*x - x  # y = 1/3*x^3 - x

#绘制图形
plt.plot(x,y, c='b')
plt.show()
