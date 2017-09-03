"""
Gamma correction is an basic gray level transformation
Formula:

    X = 255 * (X / 255) ^ y

    X: The intensive in each pixel
    255: The max level intensive of image
    y: Gamma level
"""


import cv2
import numpy as np
from __utils__.general import show_image
from histogram.plot_histogram import use_calc_hist_in_cv2_function

image = cv2.imread('../../images/wiki.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def gamma_correction(image, gamma=1):
    # Copy gray image
    image_gray = np.copy(image)

    # Contrast stretching
    for pixel in np.nditer(image_gray, op_flags=['readwrite']):
        pixel[...] = np.round(255 * np.power(pixel/float(255), gamma))
    return image_gray


res = np.hstack((
    image,
    gamma_correction(image, gamma=2),
    gamma_correction(image, gamma=0.5)
))
show_image(res)
