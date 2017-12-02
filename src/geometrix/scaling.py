import cv2
import numpy as np


def scaling(image, scale=1, dst=None):
    """
    :param image: Gray image or RGB image
    :param scale: The scale of image.
    :param dst: The image after scaling
    :return:
    """
    # Converting RGB to Gray image
    gray = image if len(image.shape) == 2 else cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    height, width = gray.shape

    # Get the size of image after scaling
    dst_height = int(height * scale)
    dst_width = int(width * scale)

    # Init the 2D matrix
    out = np.zeros(shape=(dst_height, dst_width), dtype=np.uint8)

    for x in range(0, dst_height - 1):
        for y in range(0, dst_width - 1):
            x_dst = x + 0.5
            y_dst = y + 0.5
            float_x = x_dst / scale
            float_y = y_dst / scale
            x_source = int(float_x + 0.5)
            y_source = int(float_y + 0.5)
            out[x][y] = gray[x_source][y_source]
    dst = out
    return out
