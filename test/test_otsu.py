from unittest import TestCase

from src.__utils__.general import show_image
from src.segmentation.sobel import SobelDetectionEdge
from src.segmentation.thresholding.otsu import Otsu
import cv2


# Author: KhanhLQ
class TestOtsu(TestCase):
    def test_otsu(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        otsu = Otsu(img)
        t = otsu.otsu()
        print t
        self.assertTrue(t == 101)

    def test_otsu_1(self):
        img = cv2.imread("../asserts/images/black_and_white.jpg", 0)
        otsu = Otsu(img)
        t = otsu.otsu()
        print t
        self.assertTrue(t == 101)

    def test_threshold_with_sobel_1(self):
        img = cv2.imread("../asserts/images/elena.jpg", 0)
        otsu = Otsu(img)
        t = otsu.otsu()
        sobel = SobelDetectionEdge(img, threshold=t)
        out = sobel.sobel()
        show_image(out)

    def test_threshold_with_sobel_2(self):
        img = cv2.imread("../asserts/images/black_and_white.jpg", 0)
        otsu = Otsu(img)
        t = otsu.otsu()
        sobel = SobelDetectionEdge(img, threshold=t)
        out = sobel.sobel()
        show_image(out)
