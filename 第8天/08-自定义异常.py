# -*- coding: utf-8

class PasswordException(Exception):

    def __init__(self, pw, min_length):
        self.password = pw
        self.min_length = min_length

    def __str__(self):
        return "%s的密码错误, 密码的最小长度为%s"%(self.password, self.min_length)


def reg(username, password):
    if len(password) < 6:
        raise PasswordException(password,6)  # 抛出指定的异常
    else:
        print("用户名: %s \n密 码 : %s"%(username, password))



try:
    reg("sz","126")

except Exception as ex:
    # 两个except会按照顺序先执行第一个,
    # 如果第一个满足异常类型条件, 进入第一个except. 不会进入后面的except
    print("第一个exception")
    print(ex)
except PasswordException as ex:
    print("第二个exception")
    print(ex)