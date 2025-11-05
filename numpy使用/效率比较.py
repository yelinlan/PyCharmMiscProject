import math
import numpy as np
import time

lst = list(range(1, 100000))
arr = np.array(lst)

# 使用 time 模块测量执行时间
start_time = time.time()
for i in range(100):
    lst_result = sum([math.sqrt(item ** 2) for item in lst])
end_time = time.time()

print(f"结果: {lst_result}")
print(f"python  执行时间: {end_time - start_time:.4f} 秒")

start_time = time.time()
for i in range(100):
    lst_result1 = np.sum(np.sqrt(np.power(arr,2)))
end_time = time.time()
print(f"结果: {lst_result1}")
print(f"np  执行时间: {end_time - start_time:.4f} 秒")


