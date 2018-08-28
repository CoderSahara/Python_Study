# -*- coding:utf-8

#方法一:
name="Hello World"
i=len(name)
while i>0:
    i-=1
    print(name[i])

#方法二:
print(name[-1::-1])

print(name.index("1"))
