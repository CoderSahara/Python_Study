# -*- coding:utf-8 -*-

def get_num(n):  #获取斐波拉契数列中第n个数字的值
    if n == 1 or n == 2:
        return 1
    return get_num(n-1) + get_num(n-2)

nums = []
for i in range(1,20):
    nums.append(get_num(i))

print(nums)
