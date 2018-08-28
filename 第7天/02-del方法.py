# -*- coding:utf-8

class User():
	def __init__(self):
		super(User, self).__init__()
		print("======对象初始化======")

	def __del__(self):
		print("对象即将要被销毁, (内存回收)")


u1 = User()
u2 = u1
del u1
print("="*30)
del u2
print("="*30)
