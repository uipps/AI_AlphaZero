'''
二阶魔方复原，conda环境下，记得一定要cd进入目录，因其他目录没有文本文件，避免重新生成这些文件，很耗时。

cd /D F:/develope/python/game/mofang_rubikcube/rubiksCube2x2_AlphaZero
python main.py -s UUUURRRRLFFFDDDDFBLLBLBB
python main.py -s FFBLBRDLDUBRRFDDLRLUUUFB

'''
import argparse # 获取命令行参数
import solver as sv

#cubestring = 'FFBLBRDLDUBRRFDDLRLUUUFB'  # cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string


# 每4个一组，便于查看
def pice4(inStr):
    str_list = list(inStr)
    for i, val in enumerate(str_list):
        if ( (i+1) % 5 == 0):
            str_list.insert(i," ")
    outStr = "".join(str_list)
    return outStr

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, default='UUUURRRRLFFFDDDDFBLLBLBB', help='UUUURRRRLFFFDDDDFBLLBLBB')
    #parser.add_argument('-s', dest='y=f(x), function ', action='store',nargs='?', default='2x', type=str, required=False, help='draw y=2x')

    args = parser.parse_args()
    cubestring = args.s

    print("\r\n")
    print(" orig: " + cubestring)
    print(" cut : " + pice4(cubestring))
    print("\r\n")

    a = sv.solve(cubestring)
    print(a)

if __name__ == '__main__':
    run()
