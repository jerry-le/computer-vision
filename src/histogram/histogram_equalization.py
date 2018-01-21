import numpy as np


class HistogramEqualization:
    def __init__(self, img=None):
        self.img = img
        self.max_gray_level = np.iinfo(self.img.dtype).max + 1
        self.histogram = np.zeros(self.max_gray_level, dtype=np.int32)
        self.histogram_cumsum = np.zeros(self.max_gray_level, dtype=np.int32)
        self.possibility_of_occurrence = np.zeros(self.max_gray_level, dtype=np.float32)
        self.possibility_of_occurrence_cumsum = np.zeros(self.max_gray_level, dtype=np.float32)
        self.look_up_table = np.zeros(self.max_gray_level, dtype=np.int32)
        self.img_result = np.copy(self.img)
        pass

    def compute_histogram(self):
        for pixel in np.nditer(self.img):
            self.histogram[pixel] += 1

    def compute_histogram_cumsum(self):
        cumsum = 0
        for i in range(0, self.max_gray_level):
            cumsum += self.histogram[i]
            self.histogram_cumsum[i] = cumsum
        pass

    def compute_possibility_of_occurrence(self):
        for i in range(0, self.max_gray_level):
            p = float(self.histogram_cumsum[i]) / self.histogram_cumsum[self.max_gray_level - 1]
            self.possibility_of_occurrence[i] = p

    def compute_possibility_of_occurrence_cumsum(self):
        for i in range(0, self.max_gray_level):
            p = float(self.histogram_cumsum[i]) / self.histogram_cumsum[self.max_gray_level - 1]
            self.possibility_of_occurrence_cumsum[i] = p

    def generate_look_up_table(self):
        for i in range(0, self.max_gray_level):
            self.look_up_table[i] = self.possibility_of_occurrence[i] * self.max_gray_level
        pass

    def mapping(self):
        for pixel in np.nditer(self.img_result, op_flags=['readwrite']):
            pixel[...] = self.look_up_table[pixel]

    def get_result(self):
        if self.img_result is None:
            self.compute_histogram()
            self.compute_histogram_cumsum()
            self.compute_possibility_of_occurrence()
            self.generate_look_up_table()
            self.mapping()
        return self.img_result

    def get_possibility_of_occurrence(self):
        return self.possibility_of_occurrence
