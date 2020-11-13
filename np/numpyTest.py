# -*- coding: utf-8 -*-
import random

import numpy as np
import operator

# #简单类型数组
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
#
# print(b.ndim)
# print(a.shape)

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
# print(np.median(a))
# print(np.median(a, axis=0))
# print(np.median(a, axis=1))
# # 求平均数
# print(np.mean(a))
# print(np.mean(a, axis=0))
# print(np.mean(a, axis=1))

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
# a = np.array([[4,3,2],[2,4,1]], dtype=np.int64)
# print(np.sort(a))
# print(np.sort(a, kind="mergesort", axis=None))
# print(np.sort(a, axis=0))
# print(np.sort(a, axis=1))


# 花式索引
# arr = np.arange(32).reshape((8, 4))
# print(arr)
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
# print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

# 矩阵运算
# arr = np.arange(15).reshape((3, 5))
# print(arr)
# # 转置
# print(arr.T)
# # 计算矩阵的点积
# arr = np.random.randn(6, 3)
# print (arr)
# print (np.dot(arr.T, arr))

# a = [
#     [1, 2],
#     [3, 4]
# ]
#
# b = [
#     [5, 6],
#     [7, 8]
# ]
#
# print(a)
# print(b)
#
# print(np.dot(a, b))

# 高维度转置
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)
# print('==========分割线==============')
# print(arr.transpose((1, 0, 2)))
#
# print(arr.swapaxes(1, 0))


# x = np.random.randn(8)
# y = np.random.randn(8)
#
# print(x)
# print(y)
# # numpy.maximum计算了x和y中元素级别最大的元素。
# print(np.maximum(x, y))


# arr = np.random.randn(7) * 5
# print(arr)
# # 返回小数和整数的部分
# remainder, whole_part = np.modf(arr)
# print(remainder)
# print(whole_part)

# 求两个数组的所有坐标的笛卡儿积
# points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
# xs, ys = np.meshgrid(points, points)
# print(ys)
# # 求欧氏距离
# z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)
#
# import matplotlib.pyplot as plt
#
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()


# 三元表达式, 如果condition中为True则为第一个数组的元素否则为第二个的
# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])
# result = np.where(cond, xarr, yarr)
# print(result)

# 数据统计方法
# arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(arr)
# print(arr.cumsum(axis=0))
# print(arr.cumprod(axis=1))
# print(arr.argmax(axis=0))
# print(arr.argmin(axis=1))
#
#
# bools = np.array([False, False, True, False])
# # 如果任意的一个元素是True则为True
# print(bools.any())
# # 如果所有的元素是True则为True
# print(bools.all())


# numpy提供的排序算法
# a = np.array([[3,7],[9,1]])
# print (a)
# print (np.sort(a))
# print (np.sort(a, axis =  0))
# print (np.argsort(a, axis=0))
# # 在 sort 函数中排序字段
# dt = np.dtype([('name',  'S10'),('age',  int)])
# a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
# print (a)
# print (np.sort(a, order =  'name'))


# 获取数组中唯一的值，并且排好序
# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(np.unique(names))
# ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# print(np.unique(ints))
# print(sorted(set(names)))
#
# # 判断第一个数组中的元素是否在第二个数组中存在
# values = np.array([6, 0, 0, 3, 2, 5, 6])
# print(np.in1d(values, [2, 3, 6]))


# 线性代数函数

# 矩阵乘法


# x = np.array([[1., 2., 3.], [4., 5., 6.]])
# y = np.array([[6., 23.], [-1, 7], [8, 9]])
#
# print(x)
# print(y)
# print(x.dot(y))
#
# print(np.ones(3))
# print(np.dot(x, np.ones(3)))
# # @符（类似Python 3.5）也可以用作中缀运算符，进行矩阵乘法
# print (x @ np.ones(3))

'''
numpy.linalg中有一组标准的矩阵分解运算以及诸如求逆和行列式之类的东西。它们跟MATLAB和R等语言所使用的是相同的行业标准线性代数库，
如BLAS、LAPACK、Intel MKL（Math Kernel Library，可能有，取决于你的NumPy版本）等
'''
# from numpy.linalg import qr, inv
#
# X = np.random.randn(5, 5)
# mat = X.T.dot(X)
# print(inv(mat))
# print(mat.dot(inv(mat)))
#
# q, r = qr(mat)
# print(r)
#
# arr = np.array([
#     [1, 2],
#     [3, 4]
# ])
# print(np.swapaxes(arr, 1, 0))
# print(np.swapaxes(arr, axis1=1, axis2=0).dot(arr))



# 伪随机数
# rng = np.random.RandomState(1024)
# samples = rng.randn(4, 4)
# print(samples)


# 随机漫步
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
plt.show()