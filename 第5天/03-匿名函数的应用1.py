# -*- coding:utf-8

def test(a,b,func):
    result = func(a,b)
    return result

print(test(22,33,lambda x,y:x+y))
