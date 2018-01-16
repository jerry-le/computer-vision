import numpy as np


def add(gray, extra_intensive):
    if len(gray.shape) > 2:
        raise Exception("Image input must be gray")

    # Add more intensive to each pixel of gray image
    gray_image_more_brightness = gray + extra_intensive
    return gray_image_more_brightness


def subtract(gray, excludes):
    if len(gray.shape) > 2:
        raise Exception("Image input must be gray")

    gray = np.copy(gray)

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray, op_flags=['readwrite']):
        pixel[...] = pixel - excludes if pixel - excludes >= 0 else 0
    return gray


def multiple(gray, factor):
    if len(gray.shape) > 2:
        raise Exception("Image input must be gray")

    gray = np.copy(gray)

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray, op_flags=['readwrite']):
        pixel[...] = pixel * factor if pixel * factor < 255 else 255
    return gray


def subtract2images(gray1, gray2):
    if len(gray1.shape) > 2 or len(gray2.shape) > 2:
        raise Exception("Images input must be gray")

    if gray1.shape != gray2.shape:
        raise Exception("Images must be the same size")

    return gray1 - gray2
