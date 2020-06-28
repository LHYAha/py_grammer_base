#-*- encoding = utf-8-*-
#@Time : 2020/6/21 14:16
#@Author :Ali
#@File :funcDemo.py
#@Software : PyCharm

#1、函数的定义
#2、无参的函数
#3、有参的函数
#4、返回一个值得函数
'''
#5、返回多个值得函数
def divid(a,b):
    sh=a//b
    yu=a%b
    return sh,yu #多个返回值用逗号分隔
sh,yu = divid(9,9)
print("商：%d,余：%d"%(sh,yu))
'''
def fun1():
    print("----------------")

def fun2(num):
    i = 0
    while i<num:
        i=i+1
        fun1()

def fun3(a,b,c):
    return a+b+c

def fun4(a,b,c):
    return (fun3(a,b,c)/3)

# result = fun4(1,2,3)
# print(result)
fun2(4)