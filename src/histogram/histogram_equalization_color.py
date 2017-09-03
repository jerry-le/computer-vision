import cv2
import numpy as np
from __utils__.general import show_image


image = cv2.imread('../../images/nguocsang.jpg')
image_y_cr_cb = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

# Equalize the histogram of Y channel
image_y_cr_cb[:, :, 0] = cv2.equalizeHist(image_y_cr_cb[:, :, 0])


# Convert the YCRCB back to RGB
output = cv2.cvtColor(image_y_cr_cb, cv2.COLOR_YUV2RGB)

res = np.hstack((image, output))
show_image(res)

