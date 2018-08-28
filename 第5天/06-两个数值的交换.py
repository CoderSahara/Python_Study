# -*- coding:utf-8

a = 22
b = 33

#借用元组
a,b = b,a

#使用中间变量
c = 0
c = a
b = a
a = c
