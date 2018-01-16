import cv2
import numpy as np
from unittest import TestCase
from arithmetics import basic_arithmetics as ba


class TestBasicArithmetic(TestCase):
    def setUp(self):
        self.image_path = '../asserts/images/elena.jpg'

    def test_add_gray_success(self):
        gray = cv2.imread(self.image_path, 0)
        gray_plus_10 = ba.add(gray, 10)
        self.assertEqual(gray_plus_10.shape, gray.shape)
        self.assertTrue(np.average(gray_plus_10) > np.average(gray))

    def test_add_gray_with_color_input(self):
        img = cv2.imread(self.image_path)
        try:
            gray_plus_10 = ba.add(img, 10)
        except Exception as e:
            self.assertTrue(e, 'Image input must be array')

    def test_subtract_gray_success(self):
        gray = cv2.imread(self.image_path, 0)
        gray_subtract_10 = ba.subtract(gray, 10)
        self.assertEqual(gray_subtract_10.shape, gray.shape)
        self.assertTrue(np.average(gray_subtract_10) < np.average(gray))

    def test_multiple_gray_success(self):
        gray = cv2.imread(self.image_path, 0)
        gray_time_2 = ba.multiple(gray, 2)
        self.assertEqual(gray_time_2.shape, gray.shape)
        self.assertTrue(np.average(gray) < np.average(gray_time_2))
