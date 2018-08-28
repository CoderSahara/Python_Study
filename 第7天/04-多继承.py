# -*- coding:utf-8

class A(object):
	
	def __init__(self):
		print("AAAA___init")

	def test(self):
		print("A------test()")


class B(object):

	def __init__(self):
		print("BBB___init")

	def test(self):
		print("B------test()")


class C(A,B): #多继承

    def __init__(self):
	    super().__init__()
	    self.name = "CCC"
	    print("CCCC___init")	

    def test(self):
	    print("C-------test1()")


c = C()
#print(C.__mro__) #打印C类的继承关系
c.test()

