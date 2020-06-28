#-*- encoding = utf-8-*-
#@Time : 2020/6/21 14:55
#@Author :Ali
#@File :errorDemo.py
#@Software : PyCharm

'''
#获取错误描述
try:
    print("--------test1-------")
    f = open("123.txt","r")
    print("--------test2-------")
except (NameError,IOError)as result:
    print("产生错误了")
    print(result)

#捕获所有异常
try:
    print("--------test1-------")
    f = open("123.txt","r")
    print("--------test2-------")
except Exception as result:
    print("产生错误了")
    print(result)
'''

#try ... finally 和嵌套
import time
try:
    f = open("test.txt","r")
    try:
        while True:
            contend = f.readline()
            if len(contend)==0:
                break
            time.sleep(3)
            print(contend)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常了")
    print(result)