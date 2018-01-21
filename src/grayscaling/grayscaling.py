import cv2
import numpy as np
from __utils__.general import show_image


def convert_brg2gray(image):
    """
    Use built in function cvtColor to convert 3 dimensional array (full color image) to 2 dimensional
    array (grayscaled image)
    Under the hood, the formula to convert RBG image to gray image is:
        0.299 R + 0.587 G + 0.114 B
    :param image:
    :return: 2 dimensional array
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def convert_brg2hvs(image):
    """
    HVS stands for: Hue, Value, Saturation
    :param image:
    :return: Three dimensional array
    """
    hvs_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def convert_brg2sub_channel(image, channel):
    """
    By setting the other color channels to zeros
    :param image:
    :return: Three dimensional array
    """
    if channel == 'B':
        image[:, :, 1] = 0
        image[:, :, 2] = 0
    if channel == 'G':
        image[:, :, 0] = 0
        image[:, :, 2] = 0
    if channel == 'R':
        image[:, :, 0] = 0
        image[:, :, 1] = 0
    return image


def convert_brg2individual_channel(image, channel):
    """
    Return image with the individual color in grayscaled mode
    :param image:
    :return: Two dimensional array
    """
    B, G, R = cv2.split(image)
    if channel == 'B':
        return B
    if channel == 'G':
        return G
    if channel == 'R':
        return R


def convert_rgb(image, red, green, blue):
    res = blue * image[:, :, 0] + green * image[:, :, 1] + red * image[:, :, 2]
    return res.astype(np.uint8)


if __name__ == '__main__':
    image_path = '../../asserts/images/flower.jpg'
    img = cv2.imread(image_path)
    luminance_img = convert_rgb(img, 0.299, 0.587, 0.114)
    show_image(luminance_img)
