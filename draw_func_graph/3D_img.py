# coding: utf-8

'''
3D画图测试，python3.7


运行：
  C:/ProgramData/Anaconda3/condabin/conda activate ailearn_py37                                ( python3.7环境下)
  python F:/develope/python/study_python/draw_func_graph/3D_img.py -f "mobius_01"
  python F:/develope/python/study_python/draw_func_graph/3D_img.py -f qumianPomian_01
  python F:/develope/python/study_python/draw_func_graph/3D_img.py -f img3D1

'''

import matplotlib.pyplot as plt  #导入matplotlib库
from matplotlib.tri import Triangulation
import numpy as np               #导入numpy库
#import mpl_toolkits.axisartist as axisartist
from mpl_toolkits.mplot3d import Axes3D
import argparse


def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='mobius_01', help='draw mobius_01')
    #parser.add_argument('-f', dest='y=f(x), function ', action='store',nargs='?', default='2x', type=str, required=False, help='draw y=2x')
    parser.add_argument('-b', type=float, help='xrange, begin, default -2')
    parser.add_argument('-x', type=float, default=2, help='xrange, end, default 2')
    parser.add_argument('-y', type=float, default=2, help='y-Range, begin and end, default 2')
    parser.add_argument('--y_min', type=float, help='y-Range-min, begin, default -2')
    parser.add_argument('-s', type=float, default=0.1, help='x-step, end, default 0.1')

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

    ''' 画函数图 '''
    y=eval(yfunc)

    if 'img3D1' == yfunc:
        y(xStep, xBegin, xEnd, yMin, yMax)  # 带参数
    else:
        y()

    # 下面这些来自 https://www.codenong.com/cs109422916/
    #mobius_01()
    #qumianPomian_01()
    #jizuobiao_01()
    #xiankuangtu_01()
    #line_denggao_sanwei01()
    # line_sanwei01()

    # 下面两个来自 https://blog.csdn.net/u014636245/article/details/82799573
    #qumian_sanwei()
    #quxian_sandian()

    #img3D1(xStep, xBegin, xEnd, yMin, yMax)
    #draw_rand()

def mobius_01():
    # 绘制莫比乌斯带
    theta = np.linspace(0, 2 * np.pi, 30)
    w = np.linspace(-0.25, 0.25, 8)
    w, theta = np.meshgrid(w, theta)
    phi = 0.5 * theta
    #x-y平面内的半径
    r = 1 + w * np.cos(phi)
    x = np.ravel(r * np.cos(theta))
    y = np.ravel(r * np.sin(theta))
    z = np.ravel(w * np.sin(phi))

    tri = Triangulation(np.ravel(w), np.ravel(theta))
    ax = plt.axes(projection='3d')
    ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='viridis', linewidth=0.2)
    ax.set_xlim(-1, 1);ax.set_ylim(-1,1);ax.set_zlim(-1,1)
    plt.show()

def qumianPomian_01():
    # 曲面三角剖分
    theta = 2 * np.pi * np.random.random(1000)
    r = 6 * np.random.random(1000)
    x = np.ravel(r * np.sin(theta))
    y = np.ravel(r * np.cos(theta))
    z = f(x, y)
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)
    #plt.show() # 也可展示

    ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
    plt.show()


def jizuobiao_01():
    # 使用极坐标可以获得切片的效果
    r = np.linspace(0, 6, 20)
    theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
    r, theta = np.meshgrid(r, theta)
    X = r * np.sin(theta)
    Y = r * np.cos(theta)
    Z = f(X, Y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def xiankuangtu_01():
    # 线框图和曲面图
    # 线框图
    fig =plt.figure()
    x = np.linspace(-6,6,30)
    y = np.linspace(-6,6,30)
    X, Y = np.meshgrid(x, y)
    Z = f(X,Y)
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, color='c')
    ax.set_title('wireframe')
    plt.show()

    # 曲面图
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('surface')
    plt.show()



def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

def line_denggao_sanwei01():
    # 三维等高线图  https://www.codenong.com/cs109422916/
    x = np.linspace(-6,6,30)
    y = np.linspace(-6,6,30)
    X, Y = np.meshgrid(x, y)
    Z = f(X,Y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    #调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
    ax.view_init(60, 35)
    plt.show()


def line_sanwei01():
    # 三维线的数据 https://www.codenong.com/cs109422916/
    ax = plt.axes(projection='3d')
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    plt.show()


def qumian_sanwei():
    # 3. 三维曲面 https://blog.csdn.net/u014636245/article/details/82799573
    #fig = plt.figure()  #定义新的三维坐标轴
    ax3 = plt.axes(projection='3d')
    #定义三维数据
    xx = np.arange(-5,5,0.5)
    yy = np.arange(-5,5,0.5)
    X, Y = np.meshgrid(xx, yy)
    Z = np.sin(X)+np.cos(Y)
    #作图
    ax3.plot_surface(X,Y,Z,cmap='rainbow')
    #ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
    plt.show()


def quxian_sandian():
    # 2. 三维曲线和散点 , https://blog.csdn.net/u014636245/article/details/82799573
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    z = np.linspace(0,13,1000)
    x = 5*np.sin(z)
    y = 5*np.cos(z)
    zd = 13*np.random.random(100)
    xd = 5*np.sin(zd)
    yd = 5*np.cos(zd)
    ax1.scatter3D(xd,yd,zd, cmap='Blues')  #绘制散点图
    ax1.plot3D(x,y,z,'gray')    #绘制空间曲线
    plt.show()

def img3D1(xStep, xBegin, xEnd, yMin, yMax):
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(xBegin, xEnd, xStep)
    Y = np.arange(yMin, yMax, xStep)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()

def draw_rand():
    data = np.random.randint(0, 255, size=[40, 40, 40])
    x, y, z = data[0], data[1], data[2]
    ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #  将数据点分成三部分画，在颜色上有区分度
    ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
    ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
    ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

if __name__ == '__main__':
    run()
