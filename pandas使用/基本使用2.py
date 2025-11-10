import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

csv = pd.read_csv('titanic.csv')
print(len(csv))
print(csv.shape)
# 查看数据
print(csv.head())  # 查看前五行
print("*" * 20)
print(csv.tail())  # 查看后五行
print("*" * 20)
print(csv.sample(2))  # 随机查看一行
print("*" * 20)
print(csv.describe())  # 数据描述 统计
print("*" * 20)
print(csv.info())  # 数据信息
print("*" * 20)
print(csv.dtypes)  # 数据类型
print("*" * 20)
print(csv['Survived'].unique())  # 数据唯一值
print("*" * 20)
print(csv[["Sex", "PassengerId"]].groupby("Sex").count())  # 数据分组
print("*" * 20)
count = csv[["Pclass", "Survived", "PassengerId"]].groupby(["Pclass", "Survived"]).count()
count = count.rename(columns={"PassengerId": "Count"})
print(count)  # 数据分组
sns.barplot(x="Pclass", y="Count", hue="Survived", data=count)
plt.show()
print("*" * 20)
x = count.reset_index()
print(x)  # 重置索引为01234
print("*" * 20)
print(x.set_index(["Pclass", "Survived"]))
print("*" * 20)
notnull = (~csv["Age"].isnull())
notnull_ = csv.loc[notnull, :]
print(notnull_.head())
print("*" * 20)
# 对分组数据求统计信息
agg = ((csv[["Pclass", "Survived", "Age"]]
        .groupby(["Pclass", "Survived"]))
       .agg(["sum", "mean", "std", "min", "max", "median"]))  # 数据聚合
print(agg)  # 数据聚合
print("*" * 20)
# Series  可行可列
col = csv["Age"]
row = csv.iloc[3, :]
print(col.name)
# print(col.values)
print(col.index)
print("*" * 20)
print(row.name)
print(row.values)
print(row.index)

