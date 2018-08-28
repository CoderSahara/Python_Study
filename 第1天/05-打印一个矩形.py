# -*- coding:utf-8

x = 1 #矩形的长
y = 1 #矩形的宽

while y <= 10: #为了输出10行
    x=1
    while x <= 10: #为了在一行输出10个*
        print("*",end="")
        x+=1
    print("")
    y+=1
print("已经完成")
