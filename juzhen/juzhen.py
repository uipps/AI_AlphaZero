# -*- coding: utf-8 -*-
'''
python2, python3均可


-- 运行：
  python F:/develope/python/study_python/juzhen/juzhen.py

'''

import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(A)
#print(A.shape)

B = np.array([[1,2,3],[4,5,6],[7,8,9]])
C = np.array([[1,2],[3,4],[5,6]])
D = np.array([[2],[3],[4]])
E = A+B
F = A-B
G=A*B
I=A*D

print('A:\r\n{} \r\n\r\n'  .format(A))
print('B:\r\n{} \r\n\r\n'  .format(B))
print('C:\r\n{} \r\n\r\n'  .format(C))
print('D:\r\n{} \r\n\r\n'  .format(D))

print('E= A+B:\r\n {} \r\n\r\n'  .format(E))
print('F= A-B:\r\n {} \r\n\r\n'  .format(F))
print('G=A*B:\r\n {} \r\n\r\n'  .format(G))
print('I=A*D:\r\n {} \r\n\r\n'  .format(I))
