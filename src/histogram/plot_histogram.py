import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../images/image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey()
    cv2.destroyAllWindows()


# Easy
def use_numpy_histogram_builtin(image):
    histogram = np.histogram(image, bins=np.arange(255))
    plt.plot(histogram[0])
    plt.show()


# Hard
def calc_manual_by_for_loop(image):
    histogram = np.zeros(256, dtype=np.int32)
    for pixel in np.nditer(image):
        histogram[pixel] += 1
    plt.plot(histogram)
    plt.show()


# Use ravel
def use_calc_hist_in_cv2_function(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


# Plot each channel in Histogram
def show_each_channel_histogram(image):
    # Viewing separate color channels
    color = ('b', 'g', 'r')
    # Separate each color and plot each in histogram
    for i, col in enumerate(color):
        histogram2 = cv2.calcHist(image, [i], None, [256], [0, 256])
        plt.plot(histogram2, color=col)
        plt.xlim([0, 256])
    plt.show()


use_calc_hist_in_cv2_function(image)
# calc_manual_by_for_loop(image)
# show_each_channel_histogram(image)
