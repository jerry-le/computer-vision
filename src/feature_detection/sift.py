import cv2
import numpy as np
from __utils__.general import show_image

img = cv2.imread('../../asserts/images/zigzac.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)
show_image(img)
