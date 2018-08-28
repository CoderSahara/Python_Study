# -*- coding:utf-8 -*-

#定义了一个类
class Car:
    
    def start(self):
        print("汽车启动")

    def print_all_info(self):
        print("车的名字是:%s,颜色为:%s"%(self.name,self.color))
        
c = Car() #构建一个对象
c.name = "思域"
c.color = "橘黄色"
#c2 = Car()
c.print_all_info()
c.start()
