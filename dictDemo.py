#-*- encoding = utf-8-*-
#@Time : 2020/6/21 13:46
#@Author :Ali
#@File :dictDemo.py
#@Software : PyCharm

# info = {"name":"白离","age":"18"}

#字典的访问
# print("name=",info["name"])
# print("age=",info["age"])

#访问了不存在的键，会报错
# print(info["gender"])

#print(info.get("gender")) #只用get方法，访问不存在的键，会返回None

#print(info.get("gender","女"))#通过过get方法，没找到的时候可以设定默认值
#print(info.get("age","女")) #若是键存在，不会使用默认值

info = {"name":"白离","age":"18"}
#增
'''
newID = input("请出入一个新的id：")
info["id"] = newID
print(info)
'''

#删
#[del] del info["name"]    只删除某个键值对
# del info   删除整个字典

#[clear] 清空
# info.clear()
# print(info)

#查
# print("打印所有的键：",info.keys()) #得到所有的键
# print("打印所有的值：",info.values()) #得到所有的值
# print("打印所有的键值对：",info.items()) #得到所有的项，每一项用元组的形式打印出来

'''
#遍历所有的键
for key in info.keys():
    print(key,end="\t")
#遍历所有的值
print("\n")
for value in info.values():
    print(value,end="\t")

#遍历左右的项
print("\n")
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

#补充。使用枚举函数，同时拿到列表中的下标和元素内容
# mylist = ["d","f","g","y","h"]
# for i,x in enumerate(mylist):
#     print(i+1,x)
#改