# -*- coding:utf-8

class A(object):
	name = 'zs'

	def test1(self):
		print("------A 的 test1方法")

	@classmethod  # 类方法一定要在方法的上面加上一个修饰器(java的注解), 类方法的参数cls, 代表当前的类
	def test2(cls):
		cls.name = 'ww'
		print("-----A 的 test2方法")

	@staticmethod  # 静态方法, 属于类, 没有默认传递的参数, 也可以通过类名来调用
	def test3():
		A.name = 'ls'
		print("----A的test3静态方法")

a = A()
a.test2()
A.test2()
#print(A.name)

A.test3()
print(A.name)
