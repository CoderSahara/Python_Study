# -*- coding:utf-8

def test1(r):
	s = 3.14 * (r**2)
	print("圆的面积为:%.2f"%s)

#假设我发现一个圆,圆的半径为9.8
r = 9.8
test1(r)

#另外一个圆
test1(11.8)

a = 1
def test2(a,b): #a和b前面的test1(r) 都叫形参:特点不用在前面定义,也不会和之前定义的变量冲突
	sum = a + b
	print("%s加上%s的和为:%s"%(a,b,sum))

test2(a,20) #在调用函数的时候传给函数参数的数据叫:实参. 20是实参, a=1为实参

