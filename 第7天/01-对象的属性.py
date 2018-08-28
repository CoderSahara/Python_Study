# -*- coding:utf-8

class User():
	def __init__(self, pw):
		if len(pw) >= 6:
			#私有属性前两个下划线
			self.__password = pw
		else:
			print("密码:%s , 不符合规定"%pw)

	def __str__(self):
		return "密码为:%s"%self.__password

	def get_password(self):
		return self.__password

	#私有函数前两个下划线
	def __say_heelo():
		print(self.__password)

u1 = User("12345678")
#u1.__password = "1234567" #类的外部不能直接访问私有属性
#print(u1.get_password)
u1.__say_hello()
print(u1)
