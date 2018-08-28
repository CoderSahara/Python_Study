# -*- coding:utf-8


#f = open("test1.txt" , 'w')
#f.write("hello\tworld")
#f.close()

f = open("test1.txt" , "r")
content = f.read(5)
print(content)
f.close()
