# -*- coding:utf-8

# try:
# 	print(a)
# 	i = 1/0 # 第五行没有执行到
# except (NameError,ZeroDivisionError) as error:
#     # 捕获到异常之后不会回头继续执行之前的代码
#     print("出现名字异常了")
#     print(error)
#
# try:
#     f = open('123.txt', 'r')
# except Exception as error:
# 	print('异常:%s'%error)
# else:
# 	print('try中代码没有出现异常错误')
# 	print('File content: %s:'% f.readline(5) )

# a = "123"
# f = open("text.txt", "w")
# try:
#     f.write("hello\n")
#     f.write("world %d"%a)
#     print("开始关闭文件")
#     f.close()
# except Exception as ex:
#     print(ex)
# else: # 没有异常的情况会自动执行的代码
#     print("else")
# finally: # 最重要执行的代码, 不管前面是否出现except
#     print("finally")
#     f.close()



b = "123"
f = None
try:
    f = open("text2.txt")
    try:
        content = f.read()
        content.index("hadoop")
    except ValueError as ex:
        print(ex)
except FileNotFoundError as ex:
    print(ex)
else: # 没有异常的情况会自动执行的代码
    print("else")
finally: # 最终要执行的代码, 不管前面是否出现except
    print("finally")
    if f:
        f.close()