import cv2
from unittest import TestCase
from src.feature_detection.harris_corner_detection import find_harris_conrners
from src.geometrix.scaling import scaling
from src.__utils__.general import pickle_load_object, show_image


# Author: KhanhLQ
class TestHarrisCornerDetection(TestCase):
    def test_harris(self):
        img = cv2.imread("../asserts/images/chess_board.png")
        dst = find_harris_conrners(image=img, block_size=2, ksize=5, k=0.03)
        show_image(dst)

    def test_harris_rotate_30_degrees(self):
        image = cv2.imread("../asserts/images/chess_board.png", 0)
        rows, cols = image.shape
        M = cv2.getRotationMatrix2D((rows/2, cols/2), 30, 1)
        dst = cv2.warpAffine(image, M, (cols, rows))
        out = find_harris_conrners(image=dst)
        show_image(out)

    def test_harris_rotate_30_degrees_and_zoom_out_50_percent(self):
        image = cv2.imread("../asserts/images/chess_board.png", 0)
        scaled_image = scaling(image, scale=0.5)
        rows, cols = scaled_image.shape
        M = cv2.getRotationMatrix2D((rows/2, cols/2), 30, 1)
        dst = cv2.warpAffine(image, M, (cols, rows))
        out = find_harris_conrners(image=dst)
        show_image(out)





