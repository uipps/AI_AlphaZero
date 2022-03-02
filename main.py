#!/usr/bin/python
#coding:utf-8
'''
  三阶魔方复原，conda环境下，记得一定要cd进入目录，因其他目录没有文本文件，避免重新生成这些文件，很耗时。
  默认按照： 上 右 前 下 左 后 的顺序 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'.

1. conda python37环境下，cmd命令行下：
C:/ProgramData/Anaconda3/condabin/activate ailearn_py37

cd /D F:/develope/python/game/mofang_rubikcube/rubiksCube_AlphaZero
python main.py -s UUUUUUUUURLRRRRRRRFRFFFFFFFDDDDDDDDDLFLLLLLLLBBBBBBBBB

'''
import argparse # 获取命令行参数
import solver as sv
import os

# 1. 完好的情况，无需转动
#cubestring = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'

# 2. 进行了一次R操作。程序运行后，得出可以1步、也可以多步
#cubestring = 'UUFUUFUUFRRRRRRRRRFFDFFDFFDDDBDDBDDBLLLLLLLLLUBBUBBUBB'
# 程序运行结果： R1 U2 D2 R2 L2 U2 D2 L2 (8f)
#               R3 (1f)
# 随机测试几个翻转的
#cubestring = 'UFUUUUUBURBRRRRRRRFDFFFFFFFDDDDDDDUDLRLLLLLLLBUBBBBBLB'
#cubestring = 'UUUUUDUUURFRRRRRRRFFFFFFFDFDBDDDDDBDLRLLLLLLLBLBBBBBUB'
#cubestring = 'UUUUURUDURURRRRRRRFLFFFFFDFDBDFDDDBDLLLLLLLDLBFBBBBBUB'
#cubestring = 'UUUUURUDURURRRRRRRFLFFFFFDFDBDFDDDBDLLLLLLLDLBFBBBBBUB'

#    3.1 顶层两个角和两个棱块交换的情况 ，网上的公式是11步：R U2 R' U' R U2 L' U R' U' L (11f)  （6-8互换，3-9互换）
#cubestring = 'UUUUUUUUUBFFRRRRRRFRRFFFFFFDDDDDDDDDLLLLLLLLLRBBBBBBBB'
# 程序运行结果： R2 D3 R3 D1 R3 B2 L1 U3 L3 B2 (10f)
#    3.2) 跟上面类似，但不一样 （6-8互换，7-9互换）
#cubestring = 'UUUUUUUUUFFRRRRRRRRRLFFFFFFDDDDDDDDDLLFLLLLLLBBBBBBBBB'
# 程序运行结果： F2 D1 F1 D3 F1 L2 B3 U1 B1 L2 (10f)  至少10步，
#    3.3 顶层全部黄色，只中间三个棱块顺时针调换了位置，需要逆时针复原，CFOP-PLL方法是： F2 U' R' L F2 R L' U' F2 (9f)
#cubestring = 'UUUUUUUUURLRRRRRRRFRFFFFFFFDDDDDDDDDLFLLLLLLLBBBBBBBBB'
# F2 U3 R3 L1 F2 R1 L3 U3 F2 (9f) (吻合)

# 4. 一种不可能的情况：1个棱块位置对(U8位置)，只是颜色反了。这种情况不可能，可能是因为拆开了自己品装的。
#cubestring = 'UUUUUUUFURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
# 程序运行结果：Error: Total edge flip is wrong.

#    5.1 两个同面相对棱块位置对(U2,U8位置)，只是颜色反了。直接操作如下步骤实现棱块互换
#cubestring = 'UBUUUUUFURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'
# F1 R3 L1 D1 B2 D3 R1 L3 F1 R1 L3 F2 U2 R3 L1 (15f)
#    5.2 两个同面相邻棱块位置对(U2,U4位置或U2,U6)，只是颜色反了。
#cubestring = 'UBULUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLULLLLLLLBUBBBBBBB'
# R3 L3 U2 F3 L2 F1 U2 R1 L1 B2 U1 B2 U3 B2 (14f)

# 6.1 此种情况不可能，两个相邻棱块互换(U2-U8位置)。例如上层黄色全黄，只对面颜色反了。(报错： Wrong edge and corner parity，错误的边、角奇偶性)
#cubestring = 'UUUUUUUUURRRRRRRRRFBFFFFFFFDDDDDDDDDLLLLLLLLLBFBBBBBBB'

# 6.2 此种情况不可能，两个相邻棱块互换(U2-U8位置)，对面颜色反，顶层黄色也反了。报错同上，
#cubestring = 'UFUUUUUBURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'

# 6.3 两个相邻棱块互换(U2-U8位置)，对面颜色反，顶层黄色一个反一个没反
#cubestring = 'UFUUUUUBURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'


# 7.1 对角棱块(U2,F8位置)，位置对，颜色反了
#cubestring = 'UBUUUUUUURRRRRRRRRFFFFFFFDFDFDDDDDDDLLLLLLLLLBUBBBBBBB'
# U1 R1 L3 B3 R2 D2 R2 B1 R3 L1 U1 L2 F2 L2 U2 (15f)

# 7.2 斜对角棱块(U2-F4位置)，位置对，颜色反了
#cubestring = 'UFUUUUUBURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'


# 8.1 对角棱块互换(U2-F8位置)，
#cubestring = 'UFUUUUUBURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'

# 8.2 斜对角棱块互换(U2-F4位置)，，
#cubestring = 'UFUUUUUBURRRRRRRRRFUFFFFFFFDDDDDDDDDLLLLLLLLLBUBBBBBBB'


#cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'  # cube definition string of cube we want to solve
# See module enums.py for the format of the cube definition string

# ######################### Method 1: directly call the solve routine# #################################################
# Advantage: No network layer needed. Disadvantage: Only local usage possible.                                                                  #



# 每9个一组，便于查看
def pice9(inStr):
    str_list = list(inStr)
    for i, val in enumerate(str_list):
        if ( (i+1) % 10 == 0):
            str_list.insert(i," ")
    outStr = "".join(str_list)
    return outStr

def run():
    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, default='UUFUUFUUFRRRRRRRRRFFDFFDFFDDDBDDBDDBLLLLLLLLLUBBUBBUBB', help='cube string...')
    parser.add_argument('-d', type=str, default='', help='cube action string...') # R F d U2
    #parser.add_argument('-s', dest='y=f(x), function ', action='store',nargs='?', default='2x', type=str, required=False, help='draw y=2x')

    args = parser.parse_args()
    cubestring = args.s

    ##### 执行PHP命令行命令 begin
    dongzuo = args.d
    if (dongzuo):
        cmd_php = 'D:/php8103ntsx64/php.exe F:/develope/javascript/game_/mofang_rubikcube/morefun_uipps/rubikcube.php -g 0 -d "' + dongzuo + '"'
        
        # 需要conda/pip install commands ，才能 import commands TODO 待验证
        # output = commands.getstatusoutput(cmd_php) 
        # print(output)

        # import subprocess
        # p = subprocess.Popen(cmd_php,shell=True,stdout=subprocess.PIPE) 
        # out,err = p.communicate() 
        # for line in out.splitlines(): 
        #     print(line)

        result = os.popen(cmd_php) 
        res = result.read() 
        for line in res.splitlines(): 
            length = len(line)
            if (54 == length):
                cubestring = line
            print("  PHP得到的结果字符串是: " + line)
        #print("\r\n")
        print("     执行的PHP命令是cmd: " + cmd_php)
    ##### 执行PHP命令行命令 end

    print("\r\n")
    print(" orig: " + cubestring)
    print(" cut : " + pice9(cubestring))
    print("\r\n")

    a = sv.solve(cubestring, 20, 20)  # solve with a maximum of 20 moves and a timeout of 2 seconds for example
    print(a)

    a = sv.solve(cubestring, 1, 5)  # solve with a maximum of 1 moves and a timeout of 5 seconds for example
    print(a)

if __name__ == '__main__':
    run()
