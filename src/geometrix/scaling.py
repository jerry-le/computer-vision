import cv2
import numpy as np

from __utils__.general import show_image

image = cv2.imread('../../images/block.jpg', 0)
scale = 3

height = image.shape[0]
width = image.shape[1]

dest_height = height * scale
dest_width = width * scale

out = np.zeros(shape=(dest_height, dest_width), dtype=np.int8)

for x in range(0, dest_height - 1):
    for y in range(0, dest_width - 1):
        # x_dest = x + 0.5
        # y_dest = y + 0.5
        float_x = x / scale
        float_y = y / scale
        x_source = int(float_x + 0.5)
        y_source = int(float_y + 0.5)
        if y_source == 399:
            pass
        out[x][y] = image[x_source, y_source]

show_image(image, name='input')
show_image(out, name='output')
