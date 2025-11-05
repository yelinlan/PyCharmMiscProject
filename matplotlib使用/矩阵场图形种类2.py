import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
X, Y = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
Z = np.sin(X) * np.cos(Y)

# 创建子图布局
fig, axes = plt.subplots(2, 4, figsize=(15, 8))

# imshow(Z): 显示二维数组作为图像
axes[0, 0].imshow(Z, cmap='Blues')
axes[0, 0].set_title('imshow(Z)')
axes[0, 0].axis('off')

# pcolormesh(X, Y, Z): 绘制彩色网格图
axes[0, 1].pcolormesh(X, Y, Z, cmap='Blues')
axes[0, 1].set_title('pcolormesh(X, Y, Z)')
axes[0, 1].axis('off')

# contour(X, Y, Z): 绘制等高线图
axes[0, 2].contour(X, Y, Z, colors='blue')
axes[0, 2].set_title('contour(X, Y, Z)')
axes[0, 2].axis('off')

# contourf(X, Y, Z): 填充颜色的等高线图
axes[0, 3].contourf(X, Y, Z, cmap='Blues')
axes[0, 3].set_title('contourf(X, Y, Z)')
axes[0, 3].axis('off')

# bars(X, Y, U, V): 绘制带箭头的条形图
U, V = np.cos(X), np.sin(Y)
axes[1, 0].barbs(X, Y, U, V)
axes[1, 0].set_title('bars(X, Y, U, V)')
axes[1, 0].axis('off')

# quiver(X, Y, U, V): 绘制向量场图
axes[1, 1].quiver(X, Y, U, V)
axes[1, 1].set_title('quiver(X, Y, U, V)')
axes[1, 1].axis('off')

# streamplot(X, Y, U, V): 绘制流线图
axes[1, 2].streamplot(X, Y, U, V)
axes[1, 2].set_title('streamplot(X, Y, U, V)')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
