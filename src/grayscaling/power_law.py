import cv2
import numpy as np

from __utils__.general import show_image


def power_law(image, c=1, gamma=1):
    out = image.copy()
    for pixel in np.nditer(out, op_flags=['readwrite']):
        pixel[...] = c * np.power(pixel, gamma)
    return out


if __name__ == '__main__':
    image = cv2.imread('../../asserts/images/elena.jpg', 0)
    res = np.hstack((image, power_law(image, c=1, gamma=1.1)))
    show_image(res)
