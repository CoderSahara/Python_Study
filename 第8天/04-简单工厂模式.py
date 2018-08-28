# -*- coding:utf-8

class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, axe_type):
        print(self.name + "开始工作了")
        # person完成work, 需要使用一把斧头

        # 在原始社会, 人需要一把石斧
        # axe = StoneAxe("花岗岩斧头")
        # axe.cut_tree()

        axe = Factory.create_axe(axe_type)
        axe.cut_tree()


class Axe(object):

    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print("%s斧头开始砍树"%self.name)

class StoneAxe(Axe):

    def cut_tree(self):
        print("使用石头做的斧头砍树")

class SteelAxe(Axe):

    def cut_tree(self):
        print("使用钢铁做的斧头砍树")

class Factory(object):
    # 生产斧头, 根据用户指定的类型生产
    @staticmethod
    def create_axe(axe_type):
        if axe_type == "StoneAxe":
            return StoneAxe("花岗岩斧头")
        elif axe_type == "SteelAxe":
            return SteelAxe("加爵斧头")


p = Person("沉香")
p.work("StoneAxe")