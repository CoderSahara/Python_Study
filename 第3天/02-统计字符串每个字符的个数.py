# -*- coding:utf-8

str = input("请输入一个字符串")
res = {} # key 不可重复
for i in str:
    if i in res: #表示字符,在字符串中已经出现.把原来的统计结果加1
        res[i] = res[i] + 1
    else: #表示在字符在整个字符串中第一次出现
        res[i] = 1

print(res)
