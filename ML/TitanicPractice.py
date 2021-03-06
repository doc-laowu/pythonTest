# -*- coding: utf-8 -*-

#数据分析库
import pandas as pd
#科学计算库
import numpy as np
from pandas import Series,DataFrame

data_train = pd.read_csv("C:\\Users\\gaosen\\Downloads\\titanic_train.csv")
data_test = pd.read_csv("C:\\Users\\gaosen\\Downloads\\titanic_test.csv")

# print(data_train.head())
# print(data_test.head())
#
# print(data_train.info())
# print(data_test.info())
#
# print(data_train.describe())
# print(data_test.describe())

#Age列中的缺失值用Age中位数进行填充
data_train["Age"] = data_train['Age'].fillna(data_train['Age'].median())
data_train.describe()

# 训练

# 线性回归
from sklearn.linear_model import LinearRegression

# 训练集交叉验证，得到平均值
# from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold

# 选取简单的可用输入特征
predictors = ["Pclass", "Age", "SibSp", "Parch", "Fare"]

# 初始化现行回归算法
alg = LinearRegression()
# 样本平均分成3份，3折交叉验证
# kf = KFold(data_train.shape[0],n_folds=3,random_state=1)
kf = KFold(n_splits=3, shuffle=False, random_state=1)

predictions = []
for train, test in kf.split(data_train):
    # The predictors we're using to train the algorithm.  Note how we only take then rows in the train folds.
    train_predictors = (data_train[predictors].iloc[train, :])
    # The target we're using to train the algorithm.
    train_target = data_train["Survived"].iloc[train]
    # Training the algorithm using the predictors and target.
    alg.fit(train_predictors, train_target)
    # We can now make predictions on the test fold
    test_predictions = alg.predict(data_train[predictors].iloc[test, :])
    predictions.append(test_predictions)

# 测试

# The predictions are in three aeparate numpy arrays.	Concatenate them into one.
# We concatenate them on axis 0,as they only have one axis.
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes(only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <= .5] = 0
accuracy = sum(predictions == data_train["Survived"]) / len(predictions)
print("准确率为: ", accuracy)