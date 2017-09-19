"""
@author: KhanhLQ
Goals:
    - Rotate an image theta radius and in different positions
"""

import cv2
import numpy as np
import math
from __utils__.general import show_image

image = cv2.imread('../../images/elena.jpg', 0)
height = image.shape[0]
width = image.shape[1]

theta = math.pi / 2
root = [256,256]
rotation_matrix = np.array([[math.cos(theta), math.sin(theta)],
                            [math.cos(theta), -math.sin(theta)]
                            ])

out = image.copy()
for x in range(0, height - 1):
    for y in range(0, width - 1):
        (x_src, y_src) = rotation_matrix.dot(np.array([x - root[0],y - root[1]]))
        try:
            out[x][y] = image[int(x_src)][int(y_src)]
        except Exception as e:
            out[x][y] = 0


show_image(out)

