# Author: KhanhLQ

import math
import numpy as np
from histogram.histogram_equalization import HistogramEqualization


class Otsu:
    def __init__(self, img=None):
        self.img = img
        self.max_gray_level = np.iinfo(img.dtype).max + 1
        self.p = np.zeros(self.max_gray_level)
        self.muy = np.zeros(self.max_gray_level)
        self.omega = np.zeros(self.max_gray_level)
        self.sigma = np.zeros(self.max_gray_level)

    def otsu(self):
        self.compute_p()
        self.compute_muy()
        self.compute_omega()
        self.compute_sigma()
        return self.get_threshold()

    def compute_p(self):
        histogram = HistogramEqualization(self.img)
        histogram.compute_histogram()
        histogram.compute_histogram_cumsum()
        histogram.compute_possibility_of_occurrence()
        self.p = histogram.get_possibility_of_occurrence()

    def compute_muy(self):
        sum = 0
        for i in range(0, self.max_gray_level):
            sum += i * self.p[i]
            self.muy[i] = sum
        pass

    def compute_omega(self):
        sum = 0
        for i in range(0, self.max_gray_level):
            sum += self.p[i]
            self.omega[i] = sum
        pass

    def compute_sigma(self):
        for k in range(0, self.max_gray_level):
            numerator = np.power(self.muy[self.max_gray_level - 1] * self.omega[k] - self.muy[k], 2)
            denominator = self.omega[k] * (1 - self.omega[k])
            quotient = numerator / denominator
            self.sigma[k] = 0 if math.isnan(quotient) else quotient
        pass

    def get_threshold(self):
        return np.argmax(self.sigma)
