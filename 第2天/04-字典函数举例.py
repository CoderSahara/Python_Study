# -*- coding:utf-8

stu={"name":"sahara",
      "age":"33"}

for key in stu.keys():
    print(key)

for value in stu.values():
    print(value)

print("#"*30)

#迭代字典常用方式
for item in stu.items():
    print("key为:%s,value为:%s"%item)
    #print("%s----%s"%(a,b))

print("="*30)

#判断某个key是否在字典中
key="name"
if key in stu:
    print("%s在字典中"%key)

if stu.has_key(key): #has_key方法在python3中是不存在的
	print("%s在字典中"%key)
