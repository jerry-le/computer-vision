from unittest import TestCase
from src.segmentation.canny import CannyEdgeDetection
from src.__utils__.general import pickle_load_object, show_image
import cv2
import numpy as np


# Author: KhanhLQ
class TestCannyEdgeDetection(TestCase):
    def test_canny(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        gradient_magnitude_of_x = pickle_load_object("../asserts/pickles/elena_gradient_mag_x.pickle")
        gradient_magnitude_of_y = pickle_load_object("../asserts/pickles/elena_gradient_mag_y.pickle")
        gradient_magnitude = pickle_load_object("../asserts/pickles/elena_gradient_mag.pickle")
        canny = CannyEdgeDetection(
            img=img,
            gradient_x=gradient_magnitude_of_x,
            gradient_y=gradient_magnitude_of_y,
            gradient=gradient_magnitude
        )
        suppressed = canny.non_maximal_suppression(canny.gradient_magnitude, canny.theta)
        doubled = canny.double_thresholding(suppressed, high=100, low=50)
        show_image(np.hstack(
            (
                gradient_magnitude.astype(np.uint8),
                suppressed.astype(np.uint8),
                doubled.astype(np.uint8)
            )
        ))
        self.fail()
