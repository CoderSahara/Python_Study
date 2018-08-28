# -*- coding:utf-8 -*-

def print_menu(): #打印欢迎菜单
    print("="*35)
    print("学生名字管理系统".center(30))
    print("输入1: 表示添加学生")
    print("输入2: 查找学生名字")
    print("输入3: 修改学生名字")
    print("输入4: 删除学生")
    print("输入5: 查看所有学生")
    print("输入6: 退出")

def add_student(): #添加学生信息
    name = input("请输入学生的姓名:")
    age = input("请输入学生的年龄:")
    qq = input("请输入学生的QQ号:")
    #一个学生包括三个信息,这三个信息存到一个字典中
    stu = {} #声明一个字典变量
    stu["name"] = name
    stu["age"] = age
    stu["qq"] = qq
    global student
    students.append(stu)
    print("添加成功")

def remove_student(): #删除学生信息
    name = input("请输入要删除的学生姓名:")
    index = -1
    for i,item in enumerate(students,0):
        if item["name"] == name.strip():
            index = i
    if index != -1:
        del students[index]
        print("成功删除%s的信息"%name)
    else:
        print("学生%s的名字不存在"%name)

def search_student(name): #查找学生
    for i,item in enumerate(students,1):
        if item["name"] == name.strip():
            print("序号\t姓名\t年龄\tQQ号")
            print_student(i,item)
            return item
    else:
        print("学生%s没有找到"%name)

def print_student(i,item): #打印学生信息
    print("%s\t%s\t%s\t%s"%(i,item["name"],item["age"],item["qq"]))

def print_all_students(): #打印所有学生信息
    print("序号\t姓名\t年龄\tQQ号")
    for i,item in enumerate(students,1):
        print_student(i,item)


#一个学生包含很多信息,一个学生一个字典.学生列表用列表存储
students = [] #全局变量
def main():
    print_menu()
    while True:
        operate = input("请输入你想要的操作:")
        if operate == "1": #增
            add_student()    
        elif operate == "2": #查
            name = input("请输入要查找学生的姓名:")
            search_student(name)
        elif operate == "3": #改
            pass
        elif operate == "4": #删
            remove_student()
        elif operate == "5": #查看所有
            print_all_students()
        elif operate == "6":
            break
        else:
            print("请输入正确的操作")
            continue

#一个学生包含很多信息,一个学生一个字典.学生列表用列表存储
students = [] #全局变量
main()
