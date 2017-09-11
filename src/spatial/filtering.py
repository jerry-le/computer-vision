import cv2
import numpy as np
from __utils__.general import show_image


# Median filtering
def median_filtering(image=None, k=1):
    image = cv2.imread('../../images/elena-medium.jpg', 0)
    height = image.shape[0]
    width = image.shape[1]
    out = np.copy(image)
    for i in range(k, height - k):
        for j in range(k, width - k):
            area = np.copy(image[i - k:i + k + 1:1, j - k:j + k + 1:1])
            median_value = np.sort(area.ravel())[np.power(2 * k + 1, 2) / 2]
            out[i][j] = median_value
    res = np.hstack((image, out))
    show_image(res)


# Min filtering
def min_filtering(image=None, k=1):
    image = cv2.imread('../../images/elena-medium.jpg', 0)
    height = image.shape[0]
    width = image.shape[1]
    out = np.copy(image)
    for i in range(k, height - k):
        for j in range(k, width - k):
            area = np.copy(image[i - k:i + k + 1:1, j - k:j + k + 1:1])
            min_value = np.sort(area.ravel())[0]
            out[i][j] = min_value
    res = np.hstack((image, out))
    show_image(res)


# Max filtering
def max_filtering(image=None, k=1):
    image = cv2.imread('../../images/elena-medium.jpg', 0)
    height = image.shape[0]
    width = image.shape[1]
    out = np.copy(image)
    for i in range(k, height - k):
        for j in range(k, width - k):
            area = np.copy(image[i - k:i + k + 1:1, j - k:j + k + 1:1])
            min_value = np.sort(area.ravel())[np.power(2 * k + 1, 2) - 1]
            out[i][j] = min_value
    res = np.hstack((image, out))
    show_image(res)


median_filtering(k=1)
# min_filtering(k=1)
# max_filtering(k=1)
