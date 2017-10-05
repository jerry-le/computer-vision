"""
Find the differences between 2 gray images by subtracting
"""

import cv2
import numpy as np

from __utils__.general import show_image


# Get the subtraction
def subtract_2_images(im_left, im_right):
    return im_left - im_right


def test():
    # Read and convert to gray image
    left = cv2.imread('../../images/right_2.jpg', 0)

    # Read and convert to gray image
    right = cv2.imread('../../images/right.jpg', 0)

    # Stack input and output to view easier
    res = np.hstack((left, right, subtract_2_images(left, right)))

    show_image(res, name='The differences')
