# -*- coding:utf-8 -*-


'''
n = 4
result = 1
i = 1

while i <= 4:
    result = result * i
    i += 1

print(result)
'''

# 1、在函数的内部调用自己本身
# 2、递归函数本质是一个方法的循环调用,注意: 有可能出现死循环
# 3、一定要定义递归的边界(什么时候退出循环)
def test1(n): #定义函数就是计算数字n的阶乘
    if n == 1:
        return 1
    return n * test1(n-1)

print(test1(4))
