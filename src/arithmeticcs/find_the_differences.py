"""
Find the differences between 2 gray images by subtracting
"""

import cv2
import numpy as np

from __utils__.general import show_image

# Read and convert to gray image
left = cv2.imread('../images/right_2.jpg')
left = cv2.cvtColor(left, cv2.COLOR_RGB2GRAY)

# Read and convert to gray image
right = cv2.imread('../images/right.jpg')
right = cv2.cvtColor(right, cv2.COLOR_RGB2GRAY)

# Get the subtraction
sub_matrix = left - right

# Stack input and output to view easier
res = np.hstack((left, right, sub_matrix))

show_image(res, name='The differences')
