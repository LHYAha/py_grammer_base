#-*- codeing = utf-8-*-
#@Time : 2020/6/21 13:29
#@Author :Ali
#@File :.py
#@Software : PyCharm

#tup1 = ()#创建空的元组
# tup2 = (34) 当元组只有一个时，且元素后不加逗号，表示为一个整形
# tup3 = (34,) 这才表示只有一个元组
# tup4 = (23,45,6) 当元组个数大于2，最后一个元素不用加逗号

'''
#增
tup1 = (2,45,6)
tup2 = ("daf","adsf")
tup = tup1+tup2
print(tup)
'''
#s删
tup = (3,4,676)
print("删除之前：",tup)
del tup
print("删除之后：",tup)
