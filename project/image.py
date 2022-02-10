import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns; sns.set()

c = '0'
image_name = 'img_10007.jpg'
image_path = os.path.join(os.getcwd(), 'MNIST_DS/'+c, image_name)
print(image_path)
image = Image.open(image_path)
arr = np.asarray(image)
print(arr.shape)
print(arr[16][1])

# plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
ax = sns.heatmap(arr, annot=True, fmt="d")
plt.show()
