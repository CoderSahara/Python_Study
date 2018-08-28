# -*- coding:utf-8

class Animal(object):
	
	def __init__(self):
		self.name = "动物"
	
	def eat(self):
		print("-----吃饭-----")

	def sleep(self):
		self.name = name


class Dog(Animal):

	def __init__(self,name):
		self.name = name	

	def shout(self):
		print("-----旺旺-----")


class Cat(Animal):

	#def __init__(self):
	#	print("猫初始化了")

	def catch(self):
		print("-----抓老鼠-----")


dog = Dog("小白")
dog.eat()
cat = Cat()
print(cat.name)
