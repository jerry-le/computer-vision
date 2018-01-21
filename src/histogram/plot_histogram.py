import cv2
import numpy as np
from matplotlib import pyplot as plt


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
def show_each_channel_histogram(image, color=('b', 'g', 'r')):
    # Separate each color and plot each in histogram
    for i, col in enumerate(color):
        histogram2 = cv2.calcHist(image, [i], None, [256], [0, 256])
        plt.plot(np.squeeze(histogram2))
    plt.show()


# Plot histogram in specific channel
def plot_specific_channel(image, color='r'):
    channels = {'r': 2, 'g': 1, 'b': 0}
    plt.hist(image[:, :, channels[color]].ravel(), 256, [0, 256])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('../../asserts/images/flower.jpg')
    # show_each_channel_histogram(img, color='b')
    # calc_manual_by_for_loop(img)
    # use_calc_hist_in_cv2_function(img)
    plot_specific_channel(img, 'b')
