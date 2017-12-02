import cv2
import numpy as np
from __utils__.general import show_image

filename = '../../asserts/images/elena.jpg'
image = cv2.imread(filename=filename)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

image[dst > 0.01 * dst.max()] = [0, 0, 255]

show_image(image)



