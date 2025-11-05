import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
np.random.seed(42)
x = np.random.randn(1000)
y = np.random.randn(1000)
data = np.random.randn(100, 3)  # 用于 violinplot 和 eventplot

# 创建子图布局
fig, axes = plt.subplots(2, 4, figsize=(15, 8))

# hist(x): 直方图
axes[0, 0].hist(x, bins=20, color='blue', alpha=0.7)
axes[0, 0].set_title('hist(x)')
axes[0, 0].set_xlabel('值')
axes[0, 0].set_ylabel('频数')

# boxplot(X): 箱线图
axes[0, 1].boxplot([x[:200], x[200:400], x[400:600]], patch_artist=True,
                   boxprops=dict(facecolor='blue', alpha=0.7))
axes[0, 1].set_title('boxplot(X)')
axes[0, 1].set_ylabel('值')

# errorbar(x, y, yerr, xerr): 错误条图
x_err = np.random.rand(5) * 0.5
y_err = np.random.rand(5) * 0.5
axes[0, 2].errorbar(np.arange(5), np.random.rand(5),
                    yerr=y_err, xerr=x_err, fmt='o', ecolor='blue',
                    capsize=5, color='blue')
axes[0, 2].set_title('errorbar(x, y, yerr, xerr)')
axes[0, 2].set_xlabel('X')
axes[0, 2].set_ylabel('Y')

# violinplot(D): 小提琴图
axes[0, 3].violinplot(data, showmedians=True, showextrema=True)
axes[0, 3].set_title('violinplot(D)')
axes[0, 3].set_ylabel('值')

# eventplot(D): 事件图


# hist2d(x, y): 二维直方图
axes[1, 1].hist2d(x, y, bins=20, cmap='Blues')
axes[1, 1].set_title('hist2d(x, y)')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

# hexbin(x, y, C): 六边形箱图
axes[1, 2].hexbin(x, y, gridsize=20, cmap='Blues')
axes[1, 2].set_title('hexbin(x, y, C)')
axes[1, 2].set_xlabel('X')
axes[1, 2].set_ylabel('Y')

# pie(x): 饼图
sizes = [30, 25, 20, 15, 10]
axes[1, 3].pie(sizes, labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%',
               startangle=90, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b'])
axes[1, 3].set_title('pie(x)')

plt.tight_layout()
plt.show()
