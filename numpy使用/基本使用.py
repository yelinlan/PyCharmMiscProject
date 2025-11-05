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
