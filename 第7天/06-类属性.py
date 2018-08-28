# -*- coding:utf-8

class User(object):

	name = 'zs'  # 公共的类属性
	__password = '123456'  # 私有(隐藏)的类属性

	def __init__(self, sex, username):
		self.sex = sex
		self.username = username


class QQ_User(User):
	pass

u = User('男', 'goldbin')
# print(u.name)
# u2 = User('', 'sdfs')
# print(u2.name)	

print(QQ_User.name) # name从父类继承过来的.name属于类属性.可以直接通过类来访问,也可以通过类的对象访问
print(u.name)  # 对象属性和类属性名字一样.如果你通过对象来访问会选择对象的属性.

# 类属性修改,只能通过类来修改
u.name = 'ww'  # 本质上没有修改类属性.仅仅给该对象定义了一个对象属性name,并且赋值为'ww'
print(u.name)
print(User.name)


User.name = 'ww'  # 真正的类属性修改
print(u.name)
print(User.name)

del u.name  # 本质上删除了对象的name属性,并没有删除类的属性.

del User.name  # 真正的类属性删除
