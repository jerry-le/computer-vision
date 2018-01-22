import cv2
import numpy as np
from __utils__.general import show_image


def equalizeHistColor(img):
    # Convert BGR image to YUV
    image_y_cr_cb = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

    # Equalize the histogram of Y channel
    image_y_cr_cb[:, :, 0] = cv2.equalizeHist(image_y_cr_cb[:, :, 0])

    # Convert the YUV back to RGB
    output = cv2.cvtColor(image_y_cr_cb, cv2.COLOR_YUV2RGB)

    return output


if __name__ == '__main__':
    image = cv2.imread('../../asserts/images/nguocsang.jpg')
    output = equalizeHistColor(image)
    res = np.hstack((image, output))
    show_image(res)
