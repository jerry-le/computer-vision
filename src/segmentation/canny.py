# Author: KhanhLQ

import cv2
from __utils__.general import show_image


image = cv2.imread("../../images/elena.jpg")
mean = image.mean()
high_threshold = int(mean + mean * 0.25)
low_threshold = int(mean - mean * 0.25)
edges = cv2.Canny(image, threshold1=low_threshold, threshold2=high_threshold)
show_image(edges)
