import matplotlib.pyplot as plt

x = range(1, 10)
y1 = [i ** 2 for i in x]
y2 = [i ** 3 for i in x]

plt.plot(x, y1, "ro--", label="y=x^2")
plt.plot(x, y2, "b^--", label="y=x^3")
# 设置图表标题
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("y=x^2,y=x^3")
# 设置坐标轴刻度
plt.xticks(x)
plt.yticks(y1)
plt.yticks(y2)

# 设置坐标轴范围
plt.xlim(0, 10)
plt.ylim(0, 100)

# 显示图例
plt.legend()
# 显示网格
plt.grid()
# 显示图表
plt.show()
