# -*- coding:utf-8 -*-

class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, axe_type):
        print (self.name + "开始工作了")
        # person完成work , 需要使用一把斧头

        # 在原始社会, 人需要一把石斧头
        # axe = StoneAxe("花岗岩斧头")
        # axe.cut_tree()

        # 已经有工厂
        axe = create_axe(axe_type)
        axe.cut_tree()


class Axe(object):
    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print (self.name + "%s斧头开始砍树")


class StoneAxe(Axe):

    def cut_tree(self):
        print ("使用石头做的斧头砍树")


class SteelAxe(Axe):

    def cut_tree(self):
        print ("使用钢铁做的斧头砍树")


# 全局函数-替代了之前的工厂类
# 生产斧头, 根据用户指定的类型生产
def create_axe(axe_type):
    if axe_type == 'Stone':
        return StoneAxe('花岗岩斧头')
    elif axe_type == 'SteelAxe':
        return SteelAxe('加爵斧头')


p = Person('zs')
p.work('Stone')
