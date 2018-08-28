# -*- coding: utf-8

# 使用自己制作的模块
# import module1
#from module1 import isnull, test1

from module2 import *
from module1 import *  # 如果两个模块中方法名字相同, 则后面覆盖前面的

# a = '22'
# print(module1.isnull(''))


#print(isnull("123333"))

test1()