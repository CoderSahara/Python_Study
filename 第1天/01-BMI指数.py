# -*- coding:utf-8

h=float(input("请输入身高:"))
w=float(input("请输入体重:"))

print("小明的身高位%.2f,体重为: %.2f"%(h,w))

bmi=w/(h**2)
if bmi<18.5:
    print("过轻")
elif bmi>=18.5 and bmi<25:
    print("正常")
elif bmi>=25 and bmi<28:
    print("过重")
elif bmi>=28 and bmi<32:
    print("肥胖")
elif bmi>=32:
    print("过度肥胖")

print("小明的BMI指数为:%s"%bmi)
