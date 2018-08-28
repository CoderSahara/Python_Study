# -*- coding:utf-8 -*-

a = 400 #全局变量,可以在后面的代码中使用.

def test1():
	a = 200 #局部变量只能在该函数中使用(它的作用范围在该函数里面) 
	a += 1
	print("a的值为%s"%a)

def test2():
	# a = 300
    print("test2函数中a的值为: %s"%a)

test1()
test2()
print(a)
