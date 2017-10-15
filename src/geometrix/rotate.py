"""
@author: KhanhLQ
Goals:
    - Rotate an image theta radius and in different positions
"""

import cv2
import numpy as np
import math
from __utils__.general import show_image


def manual_rotate():
    image = cv2.imread('../../images/brain.png', 0)
    height = image.shape[0]
    width = image.shape[1]

    # clone origin image
    out = image.copy()

    theta = math.pi / 4
    root = [100, 100]
    rotation_matrix = np.array(
        [[math.cos(theta), -math.sin(theta)],
         [math.sin(theta), math.cos(theta)]])

    for x in range(0, height - 1):
        for y in range(0, width - 1):
            position_vector = np.array([
                [x - root[0]],
                [y - root[1]]
            ])
            (x_src, y_src) = rotation_matrix.dot(position_vector)
            try:
                out[x][y] = image[int(x_src)][int(y_src)]
            except Exception as e:
                out[x][y] = 0
    show_image(out)


def opencv_rotate():
    image = cv2.imread('../../images/brain.png', 0)
    rows, cols = image.shape
    M = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 1)
    dst = cv2.warpAffine(image, M, (cols, rows))
    show_image(dst)

# opencv_rotate()
manual_rotate()