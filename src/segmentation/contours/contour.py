import cv2
import numpy as np
from __utils__.general import show_image

# Load the black shapes in the white background
image = cv2.imread('../../../asserts/images/left.jpg', 0)

# Find Canny edges
edges = cv2.Canny(image, threshold1=30, threshold2=200)

# Finding Contours
image, contours, _ = cv2.findContours(image=edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image=image, contours=contours, contourIdx=1, color=(255, 0, 0), thickness=3)

show_image(image)
