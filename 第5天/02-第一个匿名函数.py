# -*- coding:utf-8

def test(a,b):
    return a+b

print(test(22,33))

func = lambda x,y : x+y

print(func(22,33))

def test1(a,b):
    return a+b

sum = lambda arg1,arg2 : arg1 + arg2

print ("Value of total : " , sum(10,20))
print ("Value of tital : " , sum(20,20))
