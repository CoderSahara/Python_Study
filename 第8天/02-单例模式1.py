# -*- coding:utf-8

class User(object):
	__instance = None

	@classmethod
	def get_Instance(cls,name):
		if not cls.__instance:  # 如果 __instance 为None
			cls.__instance = User(name)
			print("11111")
		return cls.__instance

#u1 = User('zs')
#u2 = User('ls')
u1 = User.get_instance()
u2 = User.get_instance()
print(u1 == u2)  # ==判断表达式如果返回True, 这两个对象是一个对象, 并且内存地址相同
print("u1对象的内存地址: %s\nu2对象的内存地址: %s" % (id(u1), id(u2)))
