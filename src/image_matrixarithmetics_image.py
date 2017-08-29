import cv2
import numpy as np

INPUT = '../images/image.jpg'


def show_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def show_origin_image(input):
    image = cv2.imread(input)
    show_image('origin image', image)


def add(input, includes):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image('normal gray', gray_image)

    # Add more intensive to each pixel of gray image
    gray_image_more_brightness = gray_image + includes
    show_image('normal gray plus {}'.format(includes), gray_image_more_brightness)


def subtract(input, excludes):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image('normal gray', gray_image)

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray_image, op_flags=['readwrite']):
        pixel[...] = pixel - excludes if pixel - excludes >= 0 else 0
    show_image('normal gray minus {}'.format(excludes), gray_image)


def multiple(input, factor):
    # Convert and show gray image
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image('normal gray', gray_image)

    # Add more intensive to each pixel of gray image
    for pixel in np.nditer(gray_image, op_flags=['readwrite']):
        pixel[...] = pixel * factor if pixel * factor < 255 else 255
    show_image('normal gray multiple {}'.format(factor), gray_image)

# show_origin_image(INPUT)
# add(INPUT, 100)
subtract(INPUT, 200)
# multiple(INPUT, 10)