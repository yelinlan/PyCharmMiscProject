import pandas as pd

# 创建表格
workout_dict = {'日期': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'],
                '姓名': ['小王', '小王', '小王', '小王'],
                '运动项目': ['跑步', 'cycling', ' jogging', ' jogging'],
                '运动时间': [5, 10, 15, 20]}
# 创建DataFrame
workout_df = pd.DataFrame(workout_dict)
print("*" * 20)
# 查看列名
print(workout_df.columns)
print("*" * 20)
# 查看索引
print(workout_df.index)
print("*" * 20)
# 查看列名列表
print(workout_df.columns.tolist())
print("*" * 20)
# 查看索引列表
print(workout_df.index.tolist())
print("*" * 20)
# 查看数据
print(workout_df)
print("*" * 20)
# 修改 索引
workout_df.index = ["一号机", "二号机", "三号机", "四号机"]
print(workout_df)
print("*" * 20)
# 修改列名
workout_df.columns = ["日期1", "姓名1", "运动项目1", "运动时间1"]
print(workout_df)
print("*" * 20)
# 修改列名
workout_df = workout_df.rename(
    columns={"日期1": "日期", "姓名1": "姓名", "运动项目1": "运动项目", "运动时间1": "运动时间"})
print(workout_df)
print("*" * 20)
# 数据转换
to_dict = workout_df.to_dict()
print(to_dict)
print("*" * 20)
# 数据转换
to_json = workout_df.to_json()
print(to_json)
print("*" * 20)
# 数据转换
from_dict = pd.DataFrame(workout_dict, index=["初号机", "2号机", "3号机", "4号机"])
print(from_dict)
print("*" * 20)
# 获取列 序列形式
workout_df_ = workout_df["运动项目"]
print(workout_df_)
print("*" * 20)
print(type[workout_df_])
print("*" * 20)
# 获取多列 表格形式
print(workout_df[["运动项目", "运动时间"]])
print("*" * 20)
# 取数据 行名
print(workout_df.loc["一号机", :])
print("*" * 20)
print(workout_df.loc[["一号机", "二号机"], :])
print("*" * 20)
# 取数据 索引
print(workout_df.iloc[0, :])
print("*" * 20)
print(workout_df.iloc[[0, 1], :])
print("*" * 20)
print(workout_df.iloc[1:2, 1:3])  # [1,2)
print("*" * 20)
# 取某一个数据 at
print(workout_df.iloc[0, 0])
print(workout_df.at["一号机", "日期"])
