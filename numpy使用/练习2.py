import matplotlib.image as im
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 4, figsize=(15, 8))

# 拆分为RBG
lena = im.imread("lena无损原图/lena_c.bmp")
copy = lena.copy()
copy[:, :, [1, 2]] = 0
im.imsave("lena无损原图/lena_r.bmp", copy)

copy = lena.copy()
copy[:, :, [0, 2]] = 0
im.imsave("lena无损原图/lena_g.bmp", copy)

copy = lena.copy()
copy[:, :, [0, 1]] = 0
im.imsave("lena无损原图/lena_b.bmp", copy)

# 读取RGB
lena_r = im.imread("lena无损原图/lena_r.bmp")
lena_g = im.imread("lena无损原图/lena_g.bmp")
lena_b = im.imread("lena无损原图/lena_b.bmp")

# 显示红色通道
axes[0, 0].matshow(lena_r, cmap='Reds', vmin=0, vmax=255)
axes[0, 0].set_title('R')
axes[0, 0].axis('off')

# 显示绿色通道
axes[0, 1].matshow(lena_g, cmap='Greens', vmin=0, vmax=255)
axes[0, 1].set_title('G')
axes[0, 1].axis('off')

# 显示蓝色通道
axes[0, 2].matshow(lena_b, cmap='Blues', vmin=0, vmax=255)
axes[0, 2].set_title('B')
axes[0, 2].axis('off')

# rgb = np.array([lena_r, lena_g, lena_b]).astype(int)
# rgb = np.swapaxes(rgb, 0, 2) # 012->210
# rgb = np.swapaxes(rgb, 0, 1)  # 210->120
# rgb = np.moveaxis(rgb, [0, 1, 2], [2, 0, 1])  # 012->120  直接指定位序
# 合并通道

copy_ = lena_r.copy() + lena_g.copy() + lena_b.copy()

axes[0, 3].matshow(copy_, cmap='Greys_r', vmin=0, vmax=255)
axes[0, 3].set_title('RGB ')
axes[0, 3].axis('off')
plt.show()
