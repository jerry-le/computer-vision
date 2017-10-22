from unittest import TestCase
from src.segmentation.sobel import SobelDetectionEdge
from src.__utils__.general import show_image, pickle_load_object, pickle_dump_object
import cv2
import numpy as np


# Author: KhanhLQ
class TestSobelDetectionEdge(TestCase):
    def test_sobel_1(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        sobel = SobelDetectionEdge(img=img, threshold=100)
        out = sobel.sobel()
        show_image(out)

    def test_sobel_2(self):
        img = cv2.imread("../asserts/images/flower.jpg", 0)
        sobel = SobelDetectionEdge(img=img, threshold=100)
        out = sobel.sobel()
        show_image(out)

    def test_gradient_of_x(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        sobel = SobelDetectionEdge(img=img, threshold=100)
        sobel.set_gradient_of_x()
        out = sobel.get_gradient_of_x().astype(np.uint8)
        # out = sobel.get_gradient_of_x()
        # pickle_dump_object(out, "../asserts/pickles/elena_gradient_mag_x.pickle")
        show_image(out)

    def test_gradient_of_y(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        sobel = SobelDetectionEdge(img=img, threshold=100)
        sobel.set_gradient_of_y()
        out = sobel.get_gradient_of_y().astype(np.uint8)
        # out = sobel.get_gradient_of_y()
        # pickle_dump_object(out, "../asserts/pickles/elena_gradient_mag_y.pickle")
        show_image(out)

    def test_show_sobel_from_binary_file(self):
        img = pickle_load_object("../asserts/pickles/sobel_result.pickle")
        show_image(img)
