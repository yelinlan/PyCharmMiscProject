import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.sin(x) * np.cos(y)

# 创建子图布局
fig, axes = plt.subplots(2, 2, figsize=(12, 8),
                         facecolor='gray')

# tricontour(x, y, z): 三角形等高线图
axes[0, 0].tricontour(x, y, z, colors='blue')
axes[0, 0].set_title('tricontour(x, y, z) ')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')

# tricontourf(x, y, z): 填充颜色的三角形等高线图
axes[0, 1].tricontourf(x, y, z, cmap='Blues')
axes[0, 1].set_title('tricontourf(x, y, z)')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')

# tripcolor(x, y, z): 三角形彩色图
axes[1, 0].tripcolor(x, y, z, cmap='Blues')
axes[1, 0].set_title('tripcolor(x, y, z)')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')

# triplot(x, y): 三角形网格图
axes[1, 1].triplot(x, y, 'bo-', linewidth=0.5)
axes[1, 1].set_title('triplot(x, y)')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

plt.tight_layout()
plt.show()
