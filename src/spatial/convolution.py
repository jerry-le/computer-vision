import cv2
import numpy as np
from __utils__.general import show_image


image = cv2.imread('../../images/wiki.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# image = image.astype(np.int16)
out = np.copy(image)

# H = [[1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1]]

H = [[1, 0, 0],
     [0, 0, 0],
     [0, 0, 1]]
k = 1
height = image.shape[0]
width = image.shape[1]

for i in range(k, height - k):
    for j in range(k, width - k):
        sum = 0
        for m in range(-k, k):
            for n in range(-k, k):
                sum = sum + image[i + m][j + n] * H[k + m][k + n]
        out[i][j] = sum / 9

res = np.hstack((image, out))
show_image(res)



