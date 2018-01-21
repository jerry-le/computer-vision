import cv2
import numpy as np
from __utils__.general import show_image


def flip(img, axis=1):
    """
    Flip image by vertical or horizontal
    :param img_path:
    :param axis: 1 is vertical, 0 is horizontal
    :return:
    """
    if axis != 1 and axis != 0:
        raise Exception('Axis must be 1 for vertical flip, or 0 for horizontal flip')
    return cv2.flip(img, axis)


if __name__ == '__main__':
    image = cv2.imread('../../asserts/images/stop_sign.jpg')
    out_image = '../../asserts/images/stop_sign_flip.jpg'

    flipped_img = flip(image)
    res_img = np.hstack((image, flipped_img))

    show_image(res_img)

