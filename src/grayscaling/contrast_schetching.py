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


if __name__ == '__main__':
    img = cv2.imread('../../asserts/images/wiki.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    res = contrast_schetching(img)
    show_image(np.hstack((img, res)))
