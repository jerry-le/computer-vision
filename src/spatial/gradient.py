import cv2
import numpy as np
from __utils__.general import show_image
from spatial.convolution import convolution

image = cv2.imread('../../images/elena.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

sobel_mask_x = [[1, 0, -1],
                [2, 0, -2],
                [1, 0, -1]]

sobel_mask_y = [[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]]

out_x = convolution(image, sobel_mask_x)
out_y = convolution(image, sobel_mask_y)

out_x = out_x.astype(np.uint16)
out_y = out_y.astype(np.uint16)

out = np.sqrt(np.power(out_x, 2) + np.power(out_y, 2))
out = out.astype(np.uint8)

res = np.hstack((image, out_x.astype(np.uint8), out_y.astype(np.uint8), out))

show_image(res)
