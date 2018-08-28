# -*- coding:utf-8

# -*- encoding: utf-8 -*-
def test(a,b,func):
    result = func(a,b)
    return result

#func_new = input("请输入你的操作:") #python2中的input函数把传入的当做表达式处理

func_new = input("请输入你的操作:")
func_new = eval(func_new) #通过eval()函数 把字符串转换成可以执行的python表达式

print(test(22,33,func_new))
