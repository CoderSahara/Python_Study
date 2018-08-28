# -*- coding:utf-8

names=["zs","ls","ww","sl"]
names2=["zs","ls","ww","sl"]
#第一种迭代,显示序号
j=0
print("序号\t姓名")
for i in names2:
    j+=1
    print("%d\t%s"%(j,i))

print("="*20)

#第二种枚举 enumerate 枚举
for i,item in enumerate(names,1):
    print("%d\t%s"%(i,item))
