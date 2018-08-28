# -*- coding:utf-8

print("="*30)
print("学生名字管理系统".center(30))

print("输入1: 表示添加学生")
print("输入2: 查找学生名字")
print("输入3: 修改学生名字")
print("输入4: 删除学生")
print("输入5: 退出")

students=[]
while True:
    operate=input("请输入你想要的操作:")
    if operate=="1":
        name=input("请输入添加的学生姓名:")
        students.append(name.strip())
        print(students)
    elif operate=="2":
        pass
    elif operate=="3":
        pass
    elif operate=="4":
        name=input("请输入要删除的学生姓名:")
        if name not in students:
            print("你输入的学生%s不存在"%name)
            continue
        else:
            students.remove(name)
            print(name)
    elif operate=="5":
        break
    else:
        print("请输入正确的操作")
        continue
