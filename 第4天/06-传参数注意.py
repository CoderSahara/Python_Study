# -*- coding:utf-8 -*-

def test1(x,y):
	a.replace("c","C")
	b.append(10)
	print("x变量指向的内存地址为:%s"%id(x))
	print("y变量指向的内存地址为:%s"%id(y))

a="abcefg"
b=[1,2,3]
print("a变量指向的内存地址为:%s"%id(a))
print("b变量指向的内存地址为:%s"%id(b))

test1(a,b)
