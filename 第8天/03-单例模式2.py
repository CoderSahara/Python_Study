# -*- coding:utf-8

class User(object):
	__instance = None

	def __init__(self, name):
		self.name = name
	
	def __new__(cls, name):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance

u1 = User('zs')
u2 = User('ls')

print(u1 == u2)  # ==判断表达式如果返回True, 这两个对象是一个对象, 并且内存地址相同
print("u1对象的内存地址: %s\nu2对象的内存地址: %s" % (id(u1), id(u2)))
