# 等边三角形 任意取两点距离大于外接圆半径的概率

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 5))
# 画三角形
x1 = np.cos(np.pi / 6)
y1 = np.sin(np.pi / 6)
x2 = np.cos(5 * np.pi / 6)
y2 = np.sin(5 * np.pi / 6)
x3 = np.cos(- np.pi / 2)
y3 = np.sin(- np.pi / 2)
plt.plot([x1, x2], [y1, y2])
plt.plot([x1, x3], [y1, y3])
plt.plot([x2, x3], [y2, y3])

#三点
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]

#三边
AB_Vector = [x2 - x1, y2 - y1]
BC_Vector = [x3 - x2, y3 - y2]
CA_Vector = [x1 - x3, y1 - y3]


def random_point():
    xt1 = np.random.rand()*2-1
    yt1 = np.random.rand()*2-1
    P = [xt1, yt1]
    AP_Vector = [P[0] - A[0], P[1] - A[1]]
    BP_Vector = [P[0] - B[0], P[1] - B[1]]
    CP_Vector = [P[0] - C[0], P[1] - C[1]]
    # 判断点在三角形内
    if np.cross(AB_Vector, AP_Vector) > 0 and np.cross(BC_Vector, BP_Vector) > 0 and np.cross(CA_Vector, CP_Vector) > 0:
        return P
    else:
        #否则递归
        return random_point()


# 画圆
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)

# 模拟在三角形内撒小棍
total =1000000
in_num = 0
for i in range(total):
    ax, ay = random_point()
    bx, by = random_point()
    #长度与单位圆的半径进行比较
    result = np.sqrt((ax - bx) ** 2 + (ay - by) ** 2) > 1
    if result:
        # plt.plot([ax, bx], [ay, by], 'b')
        in_num = in_num + 1
    else:
        # plt.plot([ax, bx], [ay, by], 'r')
        pass
# 统计概率
print(in_num / total)

plt.plot([0, 0], [0, -1], 'g-*')
plt.axis('equal')
plt.show()


