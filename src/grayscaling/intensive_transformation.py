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

image = cv2.imread('../../images/image.jpg')
image_intensive = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
for pixel in np.nditer(image_intensive, op_flags=['readwrite']):
    pixel[...] = 255 - pixel if 255 - pixel > 0 else 0

show_image(image_intensive)
