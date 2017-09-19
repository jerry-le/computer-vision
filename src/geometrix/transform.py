"""

"""

import cv2
import numpy as np
from __utils__.general import show_image


def transform(image, delta_x=0, delta_y=0):
    height = image.shape[0]
    width = image.shape[1]

    out = image.copy()

    for x in range(0, height - 1):
        for y in range(0, width - 1):
            try:
                x_src = x + delta_x
                y_src = y + delta_y
                out[x][y] = image[x_src][y_src]
            except Exception as e:
                out[x][y] = 0

    return out


image = cv2.imread('../../images/elena.jpg', 0)
out = transform(image, 100, -100)
res = np.hstack((image, out))
show_image(res)
