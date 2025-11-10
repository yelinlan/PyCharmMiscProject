# 赌徒困境

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(15, 8))
results = np.random.rand(200, 100)
results[results < 0.5] = -1
results[results >= 0.5] = 1
cumsum_res = np.cumsum(results, axis=1)
row, col = cumsum_res.shape
# state = np.full((row, 1), fill_value=0)

for i in range(col):
    col_sum = cumsum_res[:, i]
    loss = np.where(col_sum <= -10)
    win = np.where(col_sum >= 10)
    cumsum_res[loss, i + 1:] = -10
    cumsum_res[win, i + 1:] = 10
# 绘制  每一列为值
axes[0].plot(cumsum_res.T)

# 绘制  前十条失败者
axis_ = cumsum_res[np.nanmin(cumsum_res, axis=1) <= -10][:10]
axes[1].plot(axis_.T)
# 打印失败情况
ls = sum(np.nanmin(cumsum_res, axis=1) <= -10)
print(ls)
# 打印成功情况
s = sum(np.nanmax(cumsum_res, axis=1) >= 10)
print(s)
# 打印未知情况
u = sum((np.nanmin(cumsum_res, axis=1) > -10) & (np.nanmax(cumsum_res, axis=1) < 10))
print(u)
# 打印概率
print(ls / (ls + s + u))
print(s / (ls + s + u))
print(u / (ls + s + u))
plt.show()
