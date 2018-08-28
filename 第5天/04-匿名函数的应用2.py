# -*- coding:utf-8

stus = [{"name":"zs","age":22},{"name":"ls","age":33},{"name":"aini","age":11}]
a = [222,2,34,4,5,56,76,76,7,624,22]
#a.sort() #升序排布
#a.sort(reverse=True) #降序排序
#print(a)

stus.sort(key=lambda x : x["name"]) #匿名函数的功能:返回列表中每个元素(字典)的"name"对应的值
print(stus)
