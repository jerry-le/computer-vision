import cv2
import numpy as np
from __utils__.general import show_image


# H = [[1, 0, 0],
#      [0, 0, 0],
#      [0, 0, 1]]


def convolution(image, H):
    out = np.copy(image)
    height = image.shape[0]
    width = image.shape[1]
    k = (len(H) - 1) / 2
    sum_mask = np.ravel(H).sum()
    for i in range(k, height - k):
        for j in range(k, width - k):
            sum = 0
            for m in range(-k, k):
                for n in range(-k, k):
                    sum = sum + image[i + m][j + n] * H[k + m][k + n]
            out[i][j] = sum / sum_mask
    return out


def blur(image=None, k=None):
    image = cv2.imread('../../images/image.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Create mask matrix
    H = np.ones((2 * k + 1, 2 * k + 1))
    out = convolution(image, H)
    res = np.hstack((image, out))
    show_image(res)


def embossing(image=None, k=None):
    image = cv2.imread('../../images/image.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Create mask matrix
    H = np.zeros((2 * k + 1, 2 * k + 1))
    H[k, k] = 1

    out = convolution(image, H)
    res = np.hstack((image, out))
    show_image(res)

def sharpening(image=None):
    image = cv2.imread('../../images/image.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    H = [[0, -1, 0],
         [-1, 5, -1],
         [0, -1, 0]]
    out = convolution(image, H)
    res = np.hstack((image, out))
    show_image(res)

# blur(k=6)
# embossing(k=3)
sharpening()
