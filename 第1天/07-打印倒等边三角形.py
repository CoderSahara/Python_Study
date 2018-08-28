# -*- coding:utf-8

i=int(input("请输入行数:"))

a=0
while a<i: #假设i=4,打印4行,a从0开始,当a=3最后一次循环

    b=0
    while b<a: #打印当前行前面的空格,第一行不打印空格,第二行打印一个空格...
       print(" ",end="")
       b+=1

    c=i-a
    while c>0: #打印* , 第一行打印4个*
       print("*",end=" ")
       c-=1
    print("")
    a+=1
