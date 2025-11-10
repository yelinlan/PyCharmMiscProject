import pandas as pd


# 字符串工作流

# 自定义函数
def message(series):
    return "{}_{}".format(series["Name"], series["Survived"])


csv = pd.read_csv('titanic.csv')
csv["Name"] = csv["Name"].str.split("\\s|,").str[0]
print(csv["Name"].head(20))
print("*" * 20)
# 自定义函数
csv["Name_Survived"] = csv.apply(message, axis=1).head(20)
print(csv)
