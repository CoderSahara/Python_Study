# -*- coding:utf-8

def avg_3num(a,b,c):
	if is_number(a) and is_number(b) and is_number(c):
		return (a + b + c) / 3
	else:
		print("没法计算平均值")

def is_number(a):
    if not isinstance(a,(int,float)):
        print("传入的实参是%s,不是一个数字类型"%a)
        return False
    else:
        return True

a  = avg_3num(10,2,3)
print(a)
