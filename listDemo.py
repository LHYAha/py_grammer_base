#-*- codeing = utf-8-*-
#@Time : 2020/6/21 11:47
#@Author :Ali
#@File :.py
#@Software : PyCharm

# namelist = [] #空列表
#namelist = ["校长","飞行员","老师","医生",1,2]
# print(namelist[1])
# print(namelist[0:4])
'''
length = len(namelist)
i = 0
while i<length:
    print(namelist[i])
    i +=1
'''
'''
print("-----增加前，名单列表的数据-----")
for name in namelist:
    print(name)
#增1 【append】
nametemp = input("请添加一个数据：")
namelist.append(nametemp) #在末尾添加一个数据

print("-----增加后，名单列表的数据-----")
for name in namelist:
    print(name)
'''
'''
a = [1,2]
b = [3,4]
a.append(b)#将列表b当做一个元素，加入到列表a中
print(a)

#增2 【extend】
a.extend(b)#将b列表中的每个元素，逐一追加到a中
print(a)

#增3 【insert】
a = [1,2,3]
a.insert(1,4) #在列表a中的下标为1处，添加为4的数据
print(a)
'''

'''
#删
movieName = ["年少有你","你好天空","指环王","速度与激情","最美好的我们"]
print("-----增加前，名单列表的数据-----")
for movie in movieName:
    print(movie)
# del movieName[0] #在指定位置删除一个元素
#movieName.pop() #删除末尾的一个元素
movieName.remove("年少有你") #直接删除指定的元素
print(movieName)
'''

'''
#改
namelist = ["校长","飞行员","老师","医生",1,2]
print("-----增加前，名单列表的数据-----")
for name in namelist:
    print(name)
namelist[1] = "设计师" #直接修改特定的元素
print("-----增加后，名单列表的数据-----")
for name in namelist:
    print(name)
'''

'''
#查[in,not in]
namelist = ["校长","飞行员","老师","医生",1,2]
findName = input("请输入要查找的名字：")
if findName in namelist:
    print("在")
else:
    print("不在")

print(namelist.index("飞行员",0,5)) #可以查找指定下标范围的元素，并返回找到对应数据的下标，范围区间左闭右开
print(namelist.count("飞行员"))#统计元素出现的次数
'''
'''
#排序和反转
a = [3,5,1,8,9]
print("原顺序输出：",a)
a.reverse() #反转输出
print("反转输出：",a)
a.sort()
print("升序输出：",a)
a.sort(reverse=True)
print("降序输出：",a)
'''

'''
#嵌套，相当于二纬数组
#schoolName = [[],[],[]] #有三个元素的空列表，每个元素都是一个空列表
# schoolName = [["北京大学","清华大学"],["广州大学"],["南京大学","武汉大学"],"浙江大学"]
# print(schoolName[2][0])
import random
offices = [[],[],[]]
names = ["A","D","F","T","H","R","W","N"]
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("--"*10)
'''