import cv2
import numpy as np
from __utils__.general import show_image

filename = '../../asserts/images/shape.png'
image = cv2.imread(filename=filename)


def find_harris_conrners(image, block_size=2, ksize=5, k=0.04):
    if len(image.shape) > 2:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(src=gray, blockSize=block_size, ksize=ksize, k=k)
    dst = cv2.dilate(dst, None)
    image[dst > 0.01 * dst.max()] = [0, 0, 255]
    return image

