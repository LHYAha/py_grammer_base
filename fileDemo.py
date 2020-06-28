#-*- encoding = utf-8-*-
#@Time : 2020/6/21 14:32
#@Author :Ali
#@File :fileDemo.py
#@Software : PyCharm

f = open("test.txt","r")
# f.write("hello world ,i am here")
# contend = f.read(5)
# print(contend)
'''
i = 1
contend = f.readlines() #一次性读取全部文件为列表，每行一个字符串元素
for temp in contend:
    print("第%d行，%s"%(i,temp))
    i=i+1
f.close()

contend = f.readline()#一次性读一行
print(contend)
contend = f.readline()
print(contend)
'''
f.close()
