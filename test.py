# python F:/develope/python/study/test.py
# python -c 'import time; '

import numpy
import time

# res = ''.join(str.split())
# print(res)

#time1 = time.time();
print(time.localtime(time.time()))

print(time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))

