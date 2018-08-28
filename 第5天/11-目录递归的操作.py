# -*- coding:utf-8

import os

#从/home/python 目录下找包含有hello的py文件是哪些?

#包含有hello的所有py文件列表
file_list = []

#递归函数,该函数中所有的文件路径全部采用绝对路径,parent_dir: 文件所在父目录的绝对路径, file_name表示当前你要处理的文件或者目录
def find_hello(parent_dir,file_name):
    file_abspath = os.path.join(parent_dir,file_name) #当前正在处理的文件或者目录的绝对路径
    if os.path.isdir(file_abspath): #判断传入的文件是一个目录
        for f in os.listdir(file_abspath): #进入目录,列出该目录下所有文件列表
            find_hello(file_abspath,f) #递归调用自己本身的函数
    else:
        if file_abspath.endswith(".py"): #如果传入的dir就是文件,判断文件名是否以.py结尾
            if read_and_find_hello(file_abspath): #读取该py结尾的文件,并且看看文件内容中是否包含有hello
                file_list.append(file_abspath)

#该函数主要功能:读取py结尾的文件,并且看看文件内容中是否包含有hello,如果有返回True,否则返回False
def read_and_find_hello(py_file):
    flag = False #定义一个是否包含有hello的标记变量,默认文件中不包含hello为False
    f = open(py_file) #打开文件
    while True: #由于是一行一行的读取文件,所以需要无限循环
        line = f.readline() #读取其中遗憾
        if line == '': #文件读到最后一行,终止循环
            break
        elif "hello" in line:
            flag = True
    f.close() #关闭文件
    return flag

#a = read_and_find_hello("/home/sahara/第五天/08-打开和关闭文件.py")
#print(a)

find_hello("/home","sahara")
print(file_list)

