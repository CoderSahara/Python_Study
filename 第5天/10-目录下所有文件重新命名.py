# -*- coding:utf-8

import os

file_list = os.listdir("test/")

for f in file_list:
    print(f)
    dest_file = "re-"+f #重新命名之后的目标文件名
    #f为原始文件名的名字,它不在工作目录(第五天),所以不能使用文件作为相对路径
    #f文件的相对路径为:test/f . 或者干脆写绝对路径
    #os.rename("test/"+f,"test/"+dest_file)

    #采用绝对路径的形势写代码
    parent_dir = os.path.abspath("test") #获得父目录的绝对路径
    #文件的绝对路径 = 父目录的绝对路径+ / + 文件名
    source_file = os.path.join(parent_dir,f)
    dest_file = os.path.join(parent_dir,dest_file)
    os.rename(source_file,dest_file)
