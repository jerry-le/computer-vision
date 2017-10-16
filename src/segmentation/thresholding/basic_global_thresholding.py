# Author: KhanhLQ

import cv2
import numpy as np


class BasicGlobalThreshold:
    def __init__(self, img=None, threshold=None):
        self.img = img
        self.threshold = threshold

    def set_threshold(self, estimate_threshold):
        self.threshold = estimate_threshold

    def get_threshold(self):
        if self.img is None or self.threshold is None:
            raise Exception('BasicGlobalThreshold requires image and threshold as the input')
        self.coverage_threshold(self.img, self.threshold)
        return self.threshold

    @staticmethod
    def coverage_threshold(img, estimate_threshold):
        threshold = 0
        while threshold != estimate_threshold:
            threshold = estimate_threshold
            lt_threshold = img[img < threshold]
            gte_threshold = img[img >= threshold]
            estimate_threshold = (sum(lt_threshold) / len(lt_threshold) + sum(gte_threshold) / len(gte_threshold)) / 2
        return threshold


