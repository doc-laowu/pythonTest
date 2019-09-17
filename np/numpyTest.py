# -*- coding: utf-8 -*-

import numpy as np

# #简单类型数组
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# b[1][1] = 100
#
# #打印矩阵维度
# print(a.shape)
# print(b.shape)
# #打印矩阵数据类型
# print(a.dtype)
#
# #复杂类型数组
# persontype = np.dtype({
#     'names':['name', 'age', 'chinese', 'math', 'english'],
#     'formats':['S32','i', 'i', 'i', 'f']})
# peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
#        ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
#     dtype=persontype)
#
# print(peoples)
# #取某一列的所有数据
# ages = peoples[:]['age']
# chineses = peoples[:]['chinese']
# maths = peoples[:]['math']
# englishs = peoples[:]['english']
#
# print(ages)
#
# print np.mean(ages)
# print np.mean(chineses)
# print np.mean(maths)
# print np.mean(englishs)

# #对数组的基本运算操作
# x1 = np.arange(1,11,2)
# x2 = np.linspace(1,9,5)
# print np.add(x1, x2) #加
# print np.subtract(x1, x2)  #减
# print np.multiply(x1, x2)  #乘
# print np.divide(x1, x2)  #除
# print np.power(x1, x2)  #n次方
# print np.remainder(x1, x2)  #取余
# print np.mod(x1, x2)  #同上取余
#
# #numpy的统计函数
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print np.amin(a)  #取最小值
# print np.amin(a,0)  #取axis=0（y轴方向的最小值）
# print np.amin(a,1)  #axis=1 (x轴方向最小值)
# print np.amax(a)
# print np.amax(a,0)
# print np.amax(a,1)

# #统计最大值和最小值
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print np.ptp(a)
# print np.ptp(a,0)
# print np.ptp(a,1)

# #统计数组的中位数和平均值
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# # 求中位数
# print np.median(a)
# print np.median(a, axis=0)
# print np.median(a, axis=1)
# # 求平均数
# print np.mean(a)
# print np.mean(a, axis=0)
# print np.mean(a, axis=1)

# #求数组的加权平均值
# a = np.array([1,2,3,4])
# wts = np.array([1,2,3,4])
# print np.average(a)
# print np.average(a,weights=wts)
#
# #统计数组中的标准差、方差
# a = np.array([1,2,3,4])
# print np.std(a) #标准差
# print np.var(a) #方差

#numpy进行排序
a = np.array([[4,3,2],[2,4,1]], dtype=np.int64)
print(np.sort(a))
print(np.sort(a, kind="mergesort", axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))



















