import matplotlib.image as im
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 4, figsize=(15, 8))

lena = im.imread("lena无损原图/lena.bmp")
axes[0, 0].matshow(lena, cmap='Greys_r', vmin=0, vmax=255)
axes[0, 0].set_title('')
axes[0, 0].axis('off')
# f = np.fliplr(lena)
f = lena[:, ::-1]
axes[0, 1].matshow(f, cmap='Greys_r', vmin=0, vmax=255)
axes[0, 1].set_title('')
axes[0, 1].axis('off')
# flipud = np.flipud(lena)
flipud = lena[::-1, :]
axes[1, 0].matshow(flipud, cmap='Greys_r', vmin=0, vmax=255)
axes[1, 0].set_title('')
axes[1, 0].axis('off')
rot_ = np.rot90(lena)
axes[0, 3].matshow(rot_, cmap='Greys_r', vmin=0, vmax=255)
axes[0, 3].set_title('')
axes[0, 3].axis('off')
rot_1 = np.rot90(lena, k=2)
axes[1, 1].matshow(rot_1, cmap='Greys_r', vmin=0, vmax=255)
axes[1, 1].set_title('')
axes[1, 1].axis('off')
plt.show()
