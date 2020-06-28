#-*- codeing = utf-8-*-
#@Time : 2020/6/21 10:07
#@Author :Ali
#@File : .py
#@Software : PyCharm

"""
1、格式化输出
print("我的名字是：%s，我的国籍是：%s"%("lhy","中国"))
age = 21
print("我的年龄是：%d 岁"%age)

print("aa","bb","cc")
print("www","baidu","com",sep=".")
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")
"""
"""
2、从终端输入
password = input("请输入密码：")
print("您刚输入的密码是：",password)

3、判断类型（从终端输入的类型都是字符串）
a = input("输入：")
print(type(a))
print("刚刚输入的内容：%s"%a)

4、类型转换
a = int("123")
print(type(a))
"""
'''
5、条件语句
if -3:
    print("True")
    print("通过缩进来输出相同的代码段")
else:
    print("False")

score = 89
if score >= 90 and score <= 100:
    print("考试等级为A")
elif score >=80 and score <90:
    print("考试等级为A")
'''
''' 
作业1
a = input("请输入：（剪刀（0），石头（1），布（2））")
a = int(a)
if a == 0:
    print("剪刀")
elif a == 1:
    print("石头")
elif a == 2:
    print("布")
'''
'''
6、引入随机库
import random  
#import A  是引入整个A模块；
#from A import B   是从A模块引入B函数;
#from A import B,C,D   从A模块引入B,C,D函数
#from A import \*   将A模块中的全部函数导入
x = random.randint(0,2) #随机生成【0,2】的随机数，包含0,1,2三个数字
print(x)
'''
'''
作业2
import random
a = input("请输入0-2中的一个数字：")
a = int(a)
if a == random.randint(0,2):
    print("平局！")
else:
    print("你输了！")
'''
'''
7、循环语句for
for i in range(0,5):
    print(i)
for i in range(0,10,3): #从0开始，到10结束，步值为3
    print(i,end="\t")

name = "hjkasdfhka"
for c in name :
    print(c,end="\t")
'''
''''
输出一个列表
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''
'''
i = 0
while i<5:
    print("当前是第%d次循环"%(i+1))
    print("i=%d"%i)
    i=i+1

i = 1
sum = 0
while i <= 100:
    sum += i
    i = i+1
print(sum)
'''
count = 0
while count <5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于等于5")
#z作业9x9乘法表
