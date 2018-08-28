# -*- coding:utf-8

def sum_2num(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        sum = a + b
        return sum #return被执行之后,不管return后面还有什么代码,都不会执行
        print("sum_2num求和%d"%sum) #这行代码不会执行
    else:
        print("警告:请检查输入的数据是否是数字类型!")

s = sum_2num("abc",2)
print(s)
