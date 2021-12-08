# 三阶魔方复原
  conda python3.7环境

## 运行方法
conda环境下，记得一定要cd进入目录，因其他目录没有文本文件，避免重新生成这些文件，很耗时。

```
cd /D F:/develope/python/game/mofang_rubikcube/rubiksCube_AlphaZero
python main.py -s UUUURRRRLFFFDDDDFBLLBLBB
python main.py -s FFBLBRDLDUBRRFDDLRLUUUFB
```

### 参数说明
- -s 按照上、右、前、下、左、后的顺序给出的字符串

### 其他说明
1. U-上、R-右、F-前、D-下、L-左、B-后
2. 恢复的标准图案请看 enums.py 文件中的图案
