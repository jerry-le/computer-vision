import cv2
import numpy as np
from __utils__.general import show_image

INPUT = '../../images/image.jpg'


def show_origin_image(input):
    image = cv2.imread(input)
    show_image(image, 'origin image')


def add(input, includes):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image(gray_image, 'normal gray')

    # Add more intensive to each pixel of gray image
    gray_image_more_brightness = gray_image + includes
    show_image(gray_image_more_brightness, 'normal gray plus {}'.format(includes), )


def subtract(input, excludes):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image(gray_image, 'normal gray')

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray_image, op_flags=['readwrite']):
        pixel[...] = pixel - excludes if pixel - excludes >= 0 else 0
    show_image(gray_image, 'normal gray minus {}'.format(excludes))


def multiple(input, factor):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image(gray_image, 'normal gray')

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray_image, op_flags=['readwrite']):
        pixel[...] = pixel * factor if pixel * factor < 255 else 255
    show_image(gray_image, 'normal gray multiple {}'.format(factor))



# show_origin_image(INPUT)
# add(INPUT, 100)
subtract(INPUT, 50)
# multiple(INPUT, 10)
