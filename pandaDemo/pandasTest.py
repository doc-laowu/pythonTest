# -*- coding: utf-8 -*-

import numpy as np, pandas as pd

# 数组操作
# arr1 = np.arange(10)
# print(arr1)
# s1 = pd.Series(arr1)
# print(s1)

# 创建dataframe
# arr2 = np.array(np.arange(12)).reshape(4,3)
# print(arr2)
# print(type(arr2))
# df1 = pd.DataFrame(arr2)
# print(df1)
# print(type(df1))

# 通过字典创建dataframe
# dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},'two':{'a':5,'b':6,'c':7,'d':8},'three':{'a':9,'b':10,'c':11,'d':12}}
# print(dic3)
# print(type(dic3))
# df3 = pd.DataFrame(dic3)
# print(df3)
# # 通过索引获取数据
# df4 = df3[['one','three']]
# print(df4)
# print(type(df4))

# 为索引设置标签
# s4 = pd.Series(np.array([1,1,2,3,5,8]))
# print(s4)
# print(s4.index)
# s4.index = ['a','b','c','d','e','f']
# print(s4)
# print(s4['a'])

# 索引自动化对齐
# s5 = pd.Series(np.array([10,15,20,30,55,80]),index = ['a','b','c','d','e','f'])
# print(s5)
#
# s6 = pd.Series(np.array([12,11,13,15,14,16]),index = ['a','c','g','b','d','f'])
# print(s6)
# print(s5 + s6)
# print(s5/s6)

# 利用pandas查询数据
stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
# # 查询前五行
# print(student.head(10))
# # 查询后10行
# print(student.tail(10))
# # 查询指定的行
# print(student.loc[[0,2,4,5,7]])
# # 查询制定的列
# print(student[['Name','Height','Weight']].head())
# print(student.loc[:,['Name','Height','Weight']].head())
# # 查询年龄在12以上的女生
# print(student[(student['Sex']=='F') & (student['Age']>12)])
# # 查询出所有12岁以上的女生姓名、身高和体重
# print(student[(student['Sex']=='F') & (student['Age']>12)][['Name','Height','Weight']])


# 利用pandas数据分析
# np.random.seed(1234)
# d1 = pd.Series(2*np.random.normal(size = 100)+3)
# d2 = np.random.f(2,4,size = 100)
# d3 = np.random.randint(1,100,size = 100)
#
# print('非空元素计算: ', d1.count()) #非空元素计算
# print('最小值: ', d1.min()) #最小值
# print('最大值: ', d1.max()) #最大值
# print('最小值的位置: ', d1.idxmin()) #最小值的位置，类似于R中的which.min函数
# print('最大值的位置: ', d1.idxmax()) #最大值的位置，类似于R中的which.max函数
# print('10%分位数: ', d1.quantile(0.1)) #10%分位数
# print('求和: ', d1.sum()) #求和
# print('均值: ', d1.mean()) #均值
# print('中位数: ', d1.median()) #中位数
# print('众数: ', d1.mode()) #众数
# print('方差: ', d1.var()) #方差
# print('标准差: ', d1.std()) #标准差
# print('平均绝对偏差: ', d1.mad()) #平均绝对偏差
# print('偏度: ', d1.skew()) #偏度
# print('峰度: ', d1.kurt()) #峰度
# print('描述性统计指标: ', d1.describe()) #一次性输出多个描述性统计指标

# 统计函数
# def stats(x):
# 	return pd.Series([x.count(),x.min(),x.idxmin(),x.quantile(.25),x.median(),x.quantile(.75),
#                       x.mean(),x.max(),x.idxmax(),x.mad(),x.var(),x.std(),x.skew(),x.kurt()],
#                      index = ['Count','Min','Whicn_Min','Q1','Median','Q3','Mean','Max',
#                               'Which_Max','Mad','Var','Std','Skew','Kurt'])
#
# df = pd.DataFrame(np.array([d1,d2,d3]).T,columns=['x1','x2','x3'])
# print(df.apply(stats))
# print(student['Sex'].describe())


# 透视图的操作
# Table1 = pd.pivot_table(student, values=['Height'], columns=['Sex'])
# print(Table1)
#
# Table2 = pd.pivot_table(student, values=['Height','Weight'], columns=['Sex'])
# print(Table2)
#
# Table3 = pd.pivot_table(student, values=['Height','Weight'], columns=['Sex','Age'])
# print(Table3)
#
# Table5 = pd.pivot_table(student, values=['Height','Weight'], columns=['Sex'],aggfunc=[np.mean,np.median,np.std])
# print(Table5)



# 多层索引
# Series的层次化索引，索引是一个二维数组，相当于两个索引决定一个值
# 有点类似于DataFrame的行索引和列索引
s = pd.Series(np.arange(1,10),index=[["a","a","a","b","b","c","c","d","d"],[1,2,3,1,2,3,1,2,3]])
print(s)
print(s.index)

#选取外层索引为a的数据
print(s['a'])
#选取外层索引为a和内层索引为1的数据
print(s['a',1])
#选取外层索引为a和内层索引为1,3的数据
print(s['a'][[1,3]])
#层次化索引的切片，包括右端的索引
print(s[['a','c']])
print(s['b':'d'])
#通过unstack方法可以将Series变成一个DataFrame
#数据的类型以及数据的输出结构都变成了DataFrame，对于不存在的位置使用NaN填充
print(s.unstack())


data = pd.DataFrame(np.random.randint(0,150,size=(8,12)),
               columns = pd.MultiIndex.from_product([['模拟考','正式考'],['数学','语文','英语','物理','化学','生物']]),
               index = pd.MultiIndex.from_product([['期中','期末'],['雷军','李斌'],['测试一','测试二']]))
print(data)

print(data['模拟考'][['语文','数学']])













