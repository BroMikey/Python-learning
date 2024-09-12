# import numpy as np
# from scipy import ndimage
# import matplotlib.pyplot as plt
# from PIL import Image

# # 打开并转换图像为灰度图
# image = Image.open("image.jpg").convert("L")
# image_array = np.array(image)

# # 应用高斯模糊
# blurred_image = ndimage.gaussian_filter(image_array, sigma=3)

# # 显示原图与模糊处理后的图像
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.title("Original Image")
# plt.imshow(image_array, cmap='gray')

# plt.subplot(1, 2, 2)
# plt.title("Blurred Image")
# plt.imshow(blurred_image, cmap='gray')

# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 原始数据点
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# 创建插值函数
f = interp1d(x, y)

# 新的数据点
x_new = np.linspace(0, 4, num=50, endpoint=True)

# 绘制插值结果
plt.plot(x, y, 'o', label='Original points')
plt.plot(x_new, f(x_new), '-', label='Interpolated curve')
plt.legend()
plt.show()
