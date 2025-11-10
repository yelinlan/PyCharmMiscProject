import pandas as pd

# 时间工作流
csv = pd.read_csv('yellow_tripdata_2022-01.csv')
csv = csv.rename(columns={"tpep_pickup_datetime": "出发时间", "tpep_dropoff_datetime": "到达时间"})
csv["出发时间"] = pd.to_datetime(csv["出发时间"])
csv["到达时间"] = pd.to_datetime(csv["到达时间"])
csv["时间间隔"] = csv["到达时间"] - csv["出发时间"]
csv["间隔秒"] = csv["时间间隔"].dt.seconds
csv["间隔分钟"] = csv["时间间隔"].dt.seconds / 60
csv["间隔小时"] = csv["间隔秒"] / 3600
csv["周末"] = csv["出发时间"].dt.weekday >= 5
# print(csv)

# plt.figure(figsize=(10, 6))
# csv["间隔小时"].plot.hist(bins=300)
# 图像大小自适应
# plt.show()
print(csv.groupby(["PULocationID"]).apply(lambda x: x["间隔分钟"].mean(),include_groups=False))