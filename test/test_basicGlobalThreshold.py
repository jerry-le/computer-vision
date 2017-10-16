import cv2
from unittest import TestCase
from src.segmentation.thresholding.basic_global_thresholding import BasicGlobalThreshold
from src.__utils__.general import show_image, pickle_load_object
from src.segmentation.sobel import SobelDetectionEdge


# Author: KhanhLQ
class TestBasicGlobalThreshold(TestCase):
    def test_coverage_threshold_1(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        global_threshold = BasicGlobalThreshold()
        t = global_threshold.coverage_threshold(img, estimate_threshold=80)
        self.assertTrue(t == 98)

    def test_coverage_threshold_2(self):
        img = cv2.imread("../asserts/images/black_and_white.jpg", 0)
        global_threshold = BasicGlobalThreshold()
        t = global_threshold.coverage_threshold(img, estimate_threshold=80)
        self.assertTrue(t == 127)

    def test_threshold_with_sobel_1(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        global_threshold = BasicGlobalThreshold()
        t = global_threshold.coverage_threshold(img, estimate_threshold=80)
        print t
        sobel = SobelDetectionEdge(img, threshold=t)
        out = sobel.sobel()
        show_image(out)

    def test_threshold_with_sobel_2(self):
        img = cv2.imread("../asserts/images/black_and_white.jpg", 0)
        global_threshold = BasicGlobalThreshold()
        t = global_threshold.coverage_threshold(img, estimate_threshold=80)
        print t
        sobel = SobelDetectionEdge(img, threshold=t)
        out = sobel.sobel()
        show_image(out)
