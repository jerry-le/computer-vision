"""
@author: KhanhLQ
Goals:
    - Rotate an image theta radius and in different positions
"""

import cv2
import numpy as np
import math
from __utils__.general import show_image


def manual_rotate(image):
    height = image.shape[0]
    width = image.shape[1]

    # clone origin image
    out = image.copy()

    theta = math.pi / 4
    root = [100, 100]
    rotation_matrix = np.array(
        [[math.cos(theta), -math.sin(theta)],
         [math.sin(theta), math.cos(theta)]])

    for x in range(0, height - 1):
        for y in range(0, width - 1):
            position_vector = np.array([
                [x - root[0]],
                [y - root[1]]
            ])
            (x_src, y_src) = rotation_matrix.dot(position_vector)
            try:
                out[x][y] = image[int(x_src)][int(y_src)]
            except Exception as e:
                out[x][y] = 0

    return out


def opencv_rotate(image=None, angle=None, scale=None):
    if image is None:
        raise Exception('Image cannot be None')
    if angle is None:
        raise Exception('Angle cannot be None')
    if scale is None:
        scale = 1
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((rows / 2, cols / 2), angle, scale)
    dst = cv2.warpAffine(image, M, (cols * 2, rows * 2))
    return dst


def rotate_without_cropped(image=None, angle=None, scale=None):
    if image is None:
        raise Exception('Image cannot be None')
    if angle is None:
        raise Exception('Angle cannot be None')
    if scale is None:
        scale = 1
    height, width = image.shape[:2]

    # Get rotation matrix for rotating around its center
    center = (width / 2, height / 2)
    rotation_mat = cv2.getRotationMatrix2D(center, angle, scale)

    radians = math.radians(angle)
    sin = math.sin(radians)
    cos = math.cos(radians)
    bound_w = int((height * abs(sin)) + (width * abs(cos)))
    bound_h = int((height * abs(cos)) + (width * abs(sin)))

    rotation_mat[0, 2] += ((bound_w / 2) - center[0])
    rotation_mat[1, 2] += ((bound_h / 2) - center[1])

    rotated_mat = cv2.warpAffine(image, rotation_mat, (bound_w, bound_h))
    return rotated_mat


if __name__ == '__main__':
    image_path = '../../asserts/images/bird.png'
    image = cv2.imread(image_path)

    # rotated_image = opencv_rotate(image=image, angle=45, scale=1)
    rotated_image = rotate_without_cropped(image=image, angle=45, scale=1)

    show_image(rotated_image)
