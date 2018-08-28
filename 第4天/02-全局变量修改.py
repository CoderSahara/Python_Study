# -*- coding:utf-8 -*-

names = ["laowang","zhangsan","lisi"]
student = {"name":"laowang"}
a = "laogao"
b = 100

def test1():
	print("原始的全局变量为:%s"%names)
	names[2] = "sahara"
	student["age"] = 23
	# a = "golbin" #定义一个函数变量
	global a
	a = "globin" #修改全局变量
	global b
	b = b + 1

test1()
print("最后的全局变量为%s"%names)
print("最后的全局变量为student:%s"%student)
print("最后的全局变量a的值为:%s"%a)
print("最后的全局变量b的值为:%s"%b)
