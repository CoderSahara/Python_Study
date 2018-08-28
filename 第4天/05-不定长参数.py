# -*- coding:utf-8 -*-

def test1(x,y,*args,z=10):
	print(x,y,z)
	print(args)
	sum = x + y + z
	for i in args:
		sum += i
	print("和为%s"%sum)

#test1(2,3,4,5,6,7,z=20)

def test2(x,*args,**kwargs):
	print(x)
	print(args)
	print(kwargs)
	sum = x
	for i in args:
		sum += i
	for i in kwargs.values():
		sum += i
	print("和为%s"%sum)

#test2(2,3,4,num1=5,num2=6)

#集合的拆包
nums = [3,4]
nums2 = {"num1":5,"num2":6}
test2(2,*nums,**nums2)

