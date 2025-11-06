import numpy as np

# 列表与np数组转换
array = np.array([1, 2, 3, 4, 5])
print(array.shape)
print(array.size)
print(array.ndim)
print(array.tolist())
print(array)
print("-" * 20)
# 创建数组 小数也可以
arange = np.arange(1, 10, 2)
# arange = np.arange(1, 10)
# arange = np.arange(10)
print(arange.shape)
print(arange)
print("-" * 20)
# 创建数组 [ 1.  4.  7. 10.]
linspace = np.linspace(1, 10, 4)
# 排除末尾 [1.   3.25 5.5  7.75]
# linspace = np.linspace(1, 10, 4,endpoint=False)
print(linspace.shape)
print(linspace)
print("-" * 20)
# 创建二维数组
np_arange = np.arange(1, 10)
ndarray = np_arange.reshape(3, 3)
print(ndarray.shape)
print(ndarray)
print("-" * 20)

# 创建三维数组
np_arange1 = np.arange(1, 10)
# [[[1 2 3]
#   [4 5 6]
#   [7 8 9]]]
ndarray1 = np_arange1.reshape(1, 3, 3)
print(ndarray1.shape)
print(ndarray1)
print("-" * 20)

# 创建零数组
zeros = np.zeros((3, 2))
print(zeros.shape)
print(zeros)
print("-" * 20)
# 创建单位矩阵
eye = np.eye(3)
print(eye.shape)
print(eye)
print("-" * 20)
# 创建1
ones = np.ones((3, 2))
print(ones.shape)
print(ones)
print("-" * 20)
# 创建full
full = np.full((3, 2), 5)  # -inf inf 无穷大
print(full.shape)
print(full)
print("-" * 20)
full = np.full((3, 2), np.inf)  # -inf inf 无穷大
print(full.shape)
print(full)
print("-" * 20)
full = np.full((3, 2), [1, 2])  # -inf inf 无穷大
print(full.shape)
print(full)
print("-" * 20)

# 创建全1数组
like = np.ones_like(np.array([[1, 2]]))
print(like.shape)
print(like)
print("-" * 20)
# 创建全0数组
like = np.zeros_like(np.array([[1, 2]]))
print(like.shape)
print(like)
print("-" * 20)
# 创建单位矩阵
identity = np.identity(3)
print(identity.shape)
print(identity)
print("-" * 20)
# 创建单位矩阵
eye = np.eye(3, 5)
print(eye.shape)
print(eye)
print("-" * 20)
# 上/下三角矩阵
reshape = np.reshape(np.arange(1, 10), (3, 3))
print(np.triu(reshape))
print(np.tril(reshape))
print(np.tril(reshape, -1))
print("-" * 20)
# 合并维度
reshape = np.reshape(np.arange(1, 10), (1, 3, 3))
print(reshape)
# print(reshape.ravel()) # 返回引用
print(reshape.flatten())  # 返回副本
print("-" * 20)
# 精简维度
print(reshape.squeeze())
print("-" * 20)
# 交换维度
print(reshape.swapaxes(0, 1))
print("-" * 20)
print(np.arange(1, 10).reshape(3, 3))
print(np.arange(1, 10).reshape(3, 3).transpose())
print("-" * 20)
# 矩阵拼接
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(np.concatenate((a.reshape(1, -1), b.reshape(1, -1)), axis=0))
print(np.concatenate((a.reshape(1, -1), b.reshape(1, -1)), axis=1))
print("-" * 20)
# 矩阵选取
a = np.arange(1, 10).reshape(3, 3)
print(a)
print(a[0])
print(a[0, 0])
print(a[0][0])
print(a[:, 0])
print(a[0:2, 0:2])  # 切片 [0,2)
print(a[a > 5])
print(a[(a > 5) & (a < 8)])
print(a[(a > 5) | (a < 2)])
print(a[np.logical_and(a > 5, a < 8)])
print(a[np.logical_or(a > 5, a < 2)])
print(a[:, [0, 2]])
print(a[[0, 2], [0, 2]])  # 取(0,0)  (2,2)
print("-" * 20)
print(a[[0, 2], :][:, [0, 2]])  # 0,2行 与 0，2列交点元素
print("-" * 20)
# 对角线
print(np.diag(a))
print("-" * 20)
# where
print(np.where(a > 5, a, -1))  # 满足条件返回a，否则返回-1
print(np.where(a > 5, -1, a))  # 满足条件返回-1，否则返回a
print(np.where(a > 5, a, np.where(a < 2, -1, a)))  # 多个条件
np_where = np.where(a > 5)
print(np_where)
print(a[np_where])
print(np.argwhere(a > 5))
print("-" * 20)
# 特殊数值
c = np.array([np.inf, np.nan, 0, np.e, np.pi])
print(c)
print(np.isinf(c))
print(np.isnan(c))
print(np.where(np.isnan(c)))
print(np.where(np.isinf(c)))
print("-" * 20)
# 矩阵四则运算
a = np.arange(1, 10).reshape(3, 3)
print(a + 1)
print(a - 1)
print(a * 2)
print(a / 2)
print(a ** 2)
print(a % 2)
print(a // 2)
print(np.sin(a))
print("-" * 20)
# 求和
print(a.sum())  # 全部求和
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.cumsum())  # 累加
print(a.cumsum(axis=0))
print(a.cumsum(axis=1))
print("-" * 20)
# 向量乘法
a = np.array([0, 0, 1])
b = np.array([1, 0, 0])
# 点积（内积，标量积、数量积） [0,1]*[1,0]
print(np.dot(a, b))
print(a @ b)
print(np.vdot(a, b))  # （但对复数数组会使用共轭）
print(np.inner(a, b))
# 叉积
print(np.cross(a, b))  # 叉积（向量积）
# 外积 transpose([0,1])*[1,0]
print(np.outer(a, b))  # 计算向量a和向量b的外积，结果为矩阵
print("-" * 20)
# 维度补齐(一维)
a = np.array([1, 2, 3, 4]).reshape(2, 2)
b = np.array([0, 2]).reshape(-1, 1)
c = np.array([0, 2]).reshape(1, -1)
print(a * b)
print(a * c)
print("-" * 20)
# 数据类型
print(a.dtype)
print(a.astype(np.float64))
print(a+1j)
