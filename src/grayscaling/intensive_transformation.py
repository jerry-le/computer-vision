"""
Intensive transformation is an basic gray level transformation
Formula:

    X = 255 - X , 255 - X > 0
    X = 0 , 255 - X <= 0

    X: The intensive in each pixel
    255: The max level intensive of image
"""

import cv2
import numpy as np
from __utils__.general import show_image


def intensive(image):
    out = np.copy(image)
    for pixel in np.nditer(out, op_flags=['readwrite']):
        pixel[...] = 255 - pixel if 255 - pixel > 0 else 0
    return out
