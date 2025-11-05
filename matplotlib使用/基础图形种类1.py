import matplotlib.pyplot as plt

x = range(1, 10)
y1 = [i ** 2 for i in x]
y2 = [i ** 3 for i in x]

# 绘制窗口
# plt.figure(1)

# 多个子区间 绘制图表
# 折线图
plt.subplot(2, 4, 1)
plt.plot(x, y1, "ro--", label="y=x^2")
plt.plot(x, y2, "b^--", label="y=x^3")
# 散点图
plt.subplot(2, 4, 2)
plt.scatter(x, y1, label="y=x^2")
plt.scatter(x, y2, label="y=x^3")
# 柱状图
plt.subplot(2, 4, 3)
plt.bar(x, y1, label="y=x^2")
# 线段图
plt.subplot(2, 4, 4)
plt.stem(x, y1, "ro--", label="y=x^2")
# 阶梯
plt.subplot(2, 4, 5)
plt.step(x, y1, "ro--", label="y=x^2")
# 填充
plt.subplot(2, 4, 6)
plt.fill_between(x, y1, y2, label="y=x^2")

# 显示图表
plt.show()
