import cv2
import numpy as np
from __utils__.general import show_image


def convolution(image, mask):
    # initial
    out = np.copy(image)
    height = image.shape[0]
    width = image.shape[1]
    k = (len(mask) - 1) / 2
    sum_mask = np.ravel(mask).sum()
    sum_mask = 1 if sum_mask == 0 else sum_mask

    # rendering
    for i in range(k, height - k):
        for j in range(k, width - k):
            sum = 0
            for m in range(-k, k):
                for n in range(-k, k):
                    sum = sum + image[i + m][j + n] * mask[k + m][k + n]
            out[i][j] = sum / sum_mask
    return out


def blur(image=None, k=None):
    image = cv2.imread('../../images/elena.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Create mask matrix
    mask = np.ones((2 * k + 1, 2 * k + 1))
    out = convolution(image, mask)
    res = np.hstack((image, out))
    show_image(res)


def embossing(image=None, k=None):
    image = cv2.imread('../../images/elena.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Create mask matrix
    mask = np.zeros((2 * k + 1, 2 * k + 1))
    mask[0, 0] = -1
    mask[2 * k, 2 * k] = 1

    out = convolution(image, mask)
    res = np.hstack((image, out))
    show_image(res)


def sharpening(image=None):
    image = cv2.imread('../../images/elena.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    mask = [[0, -1, 0],
         [-1, 5, -1],
         [0, -1, 0]]
    out = convolution(image, mask)
    res = np.hstack((image, out))
    show_image(res)


def gaussian_blur():
    image = cv2.imread('../../images/elena.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    mask = [[1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]]
    out = convolution(image, mask)
    res = np.hstack((image, out))
    show_image(res)


# blur(k=3)
embossing(k=2)
# sharpening()
# gaussian_blur()
