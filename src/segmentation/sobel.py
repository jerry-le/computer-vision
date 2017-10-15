# Author: KhanhLQ

import cv2
import numpy as np
from __utils__.general import show_image, pickle_dump_object, pickle_load_object
from grayscaling.contrast_schetching import contrast_schetching
from grayscaling.intensive_transformation import intensive
from spatial.convolution import gaussian_blur

SX = [[-1, -2, -1],
      [0, 0, 0],
      [1, 2, 1]]

SY = [[-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]]


def calculate_convolution(image, mask):
    height = image.shape[0]
    width = image.shape[1]
    k = (len(mask) - 1) / 2
    k = int(k)

    # initialize the result
    out = np.zeros((height, width))

    # rendering
    for i in range(k, height - k):
        for j in range(k, width - k):
            sum = 0
            for m in range(-k, k + 1):
                for n in range(-k, k + 1):
                    sum = sum + image[i + m][j + n] * mask[k + m][k + n]
            out[i][j] = sum
    return out


def threshold(image, threshold):
    out = np.copy(image)
    for pixel in np.nditer(out, op_flags=['readwrite']):
        if pixel > threshold:
            pixel[...] = 255
        else:
            pixel[...] = 0
    out = out.astype(np.uint8)
    return out


def calculate_gradient_magnitude(input):
    # Remove noise by gaussian blur
    image = gaussian_blur(input)

    # calculate the derivative of x and y
    GX = calculate_convolution(image, SX)
    GY = calculate_convolution(image, SY)

    # threshold
    G = np.sqrt(np.square(GX) + np.square(GY))
    return G


def main():
    input = cv2.imread("../../images/elena.jpg", 0)

    # Remove noise by gaussian blur
    image = gaussian_blur(input)

    # calculate the derivative of x and y
    GX = calculate_convolution(image, SX)
    GY = calculate_convolution(image, SY)

    # threshold
    G = np.sqrt(np.square(GX) + np.square(GY))
    threshold_G = threshold(G, 100)

    # intensive transform G
    G_2 = intensive(threshold_G)

    # convert back to gray channel
    G_1 = contrast_schetching(G).astype(np.uint8)
    GX_1 = contrast_schetching(GX).astype(np.uint8)
    GY_1 = contrast_schetching(GY).astype(np.uint8)

    # stack result
    res = np.hstack((input, image, GX_1, GY_1, G_1, threshold_G, G_2))

    # pickle_dump_object(res, "sobel_result.pickle")

    show_image(res)


def show_result_by_file():
    res = pickle_load_object('sobel_result.pickle')
    show_image(res)

main()
# show_result_by_file()