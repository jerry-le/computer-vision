"""
Intensive transformation is an basic gray level transformation
Formula:

    X = ( 255 / (high - low) ) * ( X - low)

    X: The intensive in each pixel
    255: The max level intensive of image
    high: The highest gray level of image
    low: The lowest gray level of image

"""

import cv2
import numpy as np
from __utils__.general import show_image
from histogram.plot_histogram import use_calc_hist_in_cv2_function

image = cv2.imread('../../images/wiki.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def contrast_schetching(image):
    # Get the high and low level intensive
    high = image.max()
    low = image.min()

    # Copy gray image
    image_gray = np.copy(image)

    # Contrast stretching
    for pixel in np.nditer(image_gray, op_flags=['readwrite']):
        pixel[...] = np.round(np.abs((255 / float(high - low)) * (pixel - low)))
    return image_gray


# res = np.hstack((image, contrast_schetching(image)))
# show_image(res)
