# -*- coding:utf-8

i = 1
sum = 0

while i <= 100: #满足该条件才进入while循环内
    if i%2 == 0:
         sum += i
    else:
        pass       
    i += 1

print("从1加到100 的偶数和为%d"%sum)
