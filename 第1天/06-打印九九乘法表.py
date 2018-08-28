# -*- coding:utf-8

x=1 #一共要打印9行

while x <= 9: #一共要循环9次,才能打印9行,每行打印的列数和行号一样
    y=1 #代表列数
    while y <= x:
        print("%d*%d=%d\t"%(y,x,x*y),end="")
        y+=1
    print("")
    x+=1
print("结束")
