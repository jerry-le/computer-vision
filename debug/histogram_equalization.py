import cv2
import numpy as np
from matplotlib import pyplot as plt
from plot_histogram import *

image = cv2.imread('../images/wiki.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def manual_histogram_equalization(image):
    # Calc the histogram of image
    histogram = np.zeros(256, dtype=np.int32)
    for pixel in np.nditer(image):
        histogram[pixel] += 1

    # Histogram equalization
    max = image.shape[0] * image.shape[1]
    for i in range(0, 255):
        sum = histogram[i] + histogram[i + 1]
        histogram[i + 1] = sum if sum < max else max

    # Lookup Table
    LUT = np.round((histogram / float(max)) * 255)

    origin_image = np.copy(image)
    # Transform origin image to histogram equalization image
    for pixel in np.nditer(image, op_flags=['readwrite']):
        pixel[...] = LUT[pixel]

    res = np.hstack((origin_image, image))
    # use_calc_hist_in_cv2_function(image)
    show_image(res)


def cv2_equalize_hist(image):
    equ = cv2.equalizeHist(image)
    res = np.hstack((image, equ))  # Stacking image side-by-side
    show_image(res)


manual_histogram_equalization(image)
# cv2_equalize_hist(image)
