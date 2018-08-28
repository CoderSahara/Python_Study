# -*- coding:utf-8

print("="*35)
print("学生名字管理系统".center(30))

print("输入1: 表示添加学生")
print("输入2: 查找学生名字")
print("输入3: 修改学生名字")
print("输入4: 删除学生")
print("输入5: 查看所有学生")
print("输入6: 退出")

#一个学生包含很多信息,一个学生一个字典.学生列表用列表存储
students=[]
while True:
    operate=input("请输入你想要的操作:")
    if operate == "1":
        name = input("请输入学生的姓名:")
        age = input("请输入学生的年龄:")
        qq = input("请输入学生的QQ号:")
        
		#一个学生包括三个信息,这三个信息存到一个字典中
        stu={} #声明一个字典变量
        stu["name"]=name
        stu["age"]=age
        stu["qq"]=qq
        students.append(stu)
    elif operate=="2":
        name = input("请输入要查找学生的姓名:")
        for item in students:
            if item["name"] == name.strip():
                print("%s 学生存在,年龄为: %s,QQ号为:%s"%(item["name"],item["age"],item["qq"]))
                break
        else:
            print("学生%s没有找到"%name)
    elif operate=="3":
        pass
    elif operate=="4":
        name=input("请输入要删除的学生姓名:")
        if name not in students:
            print("你输入的学生%s不存在"%name)
            continue
        else:
            students.remove(name)
            print("成功删除%s的信息"%name)
    elif operate=="5":
        print("序号\t姓名\t年龄\tQQ号")
        for i,item in enumerate(students,1):
            print("%s\t%s\t%s\t%s"%(i,item["name"],item["age"],item["qq"]))
    elif operate=="6":
        break
    else:
        print("请输入正确的操作")
        continue
