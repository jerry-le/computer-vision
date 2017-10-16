from unittest import TestCase
from src.histogram.histogram_equalization import HistogramEqualization
from src.__utils__.general import show_image
import cv2
import numpy as np


# Author: KhanhLQ
class TestHistogramEqualization(TestCase):
    def test_compute_histogram(self):
        img = cv2.imread("../asserts/images/elena.jpg")
        histogram = HistogramEqualization(img=img)
        histogram.compute_histogram()
        histogram.compute_histogram_cumsum()
        histogram.compute_possibility_of_occurrence()
        histogram.generate_look_up_table()
        histogram.mapping()
        out = histogram.get_result()
        show_image(np.hstack((img, out)))
        self.assertTrue(False)

    def test_get_possibility_of_occurrence(self):
        img = cv2.imread("../asserts/images/elena.jpg")
        histogram = HistogramEqualization(img=img)
        histogram.get_possibility_of_occurrence()
