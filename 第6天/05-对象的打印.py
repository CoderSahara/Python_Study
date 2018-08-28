# -*- coding:utf-8 -*-

class Person():

    #初始化对象的方法,不是构建对象的方法
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "姓名:%s,年龄为:%s岁,身高为%scm"%(self.name,self.age,self.height)

    #
    def introduce(self):
        print("姓名:%s,年龄为:%s岁,身高为%scm"%(self.name,self.age,self.height))

p1 = Person('zs',18,1.77)
#p1.introduce()
print(p1)
