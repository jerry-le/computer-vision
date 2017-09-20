import cv2
import numpy as np

from __utils__.general import show_image


def scaling(image, scale=1):
    height = image.shape[0]
    width = image.shape[1]

    dest_height = int(height * scale)
    dest_width = int(width * scale)

    out = np.zeros(shape=(dest_height, dest_width), dtype=np.uint8)

    for x in range(0, dest_height - 1):
        for y in range(0, dest_width - 1):
            x_dest = x + 0.5
            y_dest = y + 0.5
            float_x = x_dest / scale
            float_y = y_dest / scale
            x_source = int(float_x + 0.5)
            y_source = int(float_y + 0.5)
            out[x][y] = image[x_source][y_source]
    return out

image = cv2.imread('../../images/shape.png', 0)
scale = 0.25

out = scaling(image, scale=scale)
show_image(out, name='output')
show_image(image, name='input')
