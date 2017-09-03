import cv2

from __utils__.general import show_image

image = cv2.imread('../images/image.jpg')


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


show_image(
    convert_brg2sub_channel(image, 'R')
)
