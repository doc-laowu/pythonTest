# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#数据读入使用pd.read_csv()
data = pd.read_csv('C:\\Users\\gaosen\\Downloads\\data_03.csv')

'''
cand_nm – 接受捐赠的候选人姓名
contbr_nm – 捐赠人姓名
contbr_st – 捐赠人所在州
contbr_employer – 捐赠人所在公司
contbr_occupation – 捐赠人职业
contb_receipt_amt – 捐赠数额（美元）
contb_receipt_dt – 收到捐款的日期
'''

#查看数据的信息，包括每个字段的名称、非空数量、字段的数据类型
# print(data.info())

#用统计学指标快速描述数据的概要
# print(data.describe())

# 数据清洗
#从data.info()得知，contbr_employer、contbr_occupation均有少量缺失值,均填充为NOT PROVIDED
# data['contbr_employer'].fillna('NOT PROVIDED',inplace=True)
# data['contbr_occupation'].fillna('NOT PROVIDED',inplace=True)


#查看数据中总统候选人都有谁
# print('共有{}位候选人，分别是'.format(len(data['cand_nm'].unique())))
# print(data['cand_nm'].unique())

#通过搜索引擎等途径，获取到每个总统候选人的所属党派，建立字典parties，候选人名字作为键，所属党派作为对应的值
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

#通过map映射函数，增加一列party存储党派信息
data['party']=data['cand_nm'].map(parties)
#查看两个党派的情况
# data['party'].value_counts()

#
# print(data.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:20])


#建立一个职业对应字典，把相同职业的不同表达映射为对应的职业，比如把C.E.O.映射为CEO
occupation_map = {
  'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
  'INFORMATION REQUESTED':'NOT PROVIDED',
  'SELF' : 'SELF-EMPLOYED',
  'SELF EMPLOYED' : 'SELF-EMPLOYED',
  'C.E.O.':'CEO',
  'LAWYER':'ATTORNEY',
}

# 如果不在字典中,返回x
# f = lambda x: occupation_map.get(x, x)
# data.contbr_occupation = data.contbr_occupation.map(f)
# print(data.contbr_occupation)

# 转换
emp_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'SELF' : 'SELF-EMPLOYED',
   'SELF EMPLOYED' : 'SELF-EMPLOYED',
}

# If no mapping provided, return x
# f = lambda x: emp_mapping.get(x, x)
# data.contbr_employer = data.contbr_employer.map(f)

# 筛选赞助金额大于0的
# data = data[data['contb_receipt_amt']>0]

#查看各候选人获得的赞助总金额
# print(data.groupby('cand_nm')['contb_receipt_amt'].sum().sort_values(ascending=False))


#选取候选人为Obama、Romney的子集数据
data_vs = data[data['cand_nm'].isin(['Perry, Rick','Romney, Mitt'])].copy()

# 面元化操作
bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])
labels = pd.cut(data_vs['contb_receipt_amt'],bins)
# print(labels)

#按照党派、职业对赞助金额进行汇总，类似excel中的透视表操作，聚合函数为sum
# by_occupation = data.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')
# print(by_occupation)
#过滤掉赞助金额小于200W的数据
# over_2mm = by_occupation[by_occupation.sum(1)<2000000]
# print(over_2mm)
#
# over_2mm.plot(kind='bar')
# plt.plot(over_2mm)
# plt.show()


# 由于职业和雇主的处理非常相似，我们定义函数get_top_amounts()对两个字段进行分析处理
def get_top_amounts(group, key, n=5):
    # 传入groupby分组后的对象，返回按照key字段汇总的排序前n的数据
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]


grouped = data_vs.groupby('cand_nm')
# print(grouped.apply(get_top_amounts, 'contbr_occupation', n=7))


#同样的，使用get_top_amounts()对雇主进行分析处理
# print(grouped.apply(get_top_amounts,'contbr_employer',n=10))

#labels是之前赞助金额离散化后的Series
grouped_bins = data_vs.groupby(['cand_nm',labels])
ret = grouped_bins.size().unstack(0)


bucket_sums=grouped_bins['contb_receipt_amt'].sum().unstack(0)
print(bucket_sums)

#Obama、Romney各区间赞助总金额
bucket_sums.plot(kind='bar')
plt.plot(bucket_sums)
plt.show()

#算出每个区间两位候选人收到赞助总金额的占比
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1),axis=0)
print(normed_sums)














