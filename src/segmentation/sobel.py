# Author: KhanhLQ

import numpy as np


class SobelDetectionEdge:
    def __init__(self, img, Sx=None, Sy=None, threshold=None):
        self.img = img
        self.Sx = Sx
        self.Sy = Sy
        self.threshold = threshold
        self.Gx = None
        self.Gy = None
        self.G = None

        if threshold is None:
            self.threshold = 100

        if Sx is None:
            self.Sx = [[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]]

        if Sy is None:
            self.Sy = [[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]]

    def get_gradient_of_x(self):
        """
        Calculate the gradient of x by convolution image with Sx
        :return:  Matrix of float
        """
        if self.Gx is None:
            self.set_gradient_of_x()
        return self.Gx

    def get_gradient_of_y(self):
        """
        Calculate the gradient of y by convolution image with Sy
        :return:  Matrix of float
        """
        if self.Gy is None:
            self.set_gradient_of_y()
        return self.Gy

    def get_gradient_magnitude(self):
        """
        Check if gradient of x and y exist then set the magnitude
        :return:
        """
        if self.Gx is not None and self.Gy is not None:
            self.set_gradient_magnitude()
        else:
            self.set_gradient_of_x()
            self.set_gradient_of_y()
            self.set_gradient_magnitude()
        return self.G

    def get_gradient_magnitude_after_thresholding(self):
        return self.thresholding(self.img, self.threshold)

    def set_gradient_of_x(self):
        self.Gx = self.calculate_convolution(self.img, self.Sx)

    def set_gradient_of_y(self):
        self.Gy = self.calculate_convolution(self.img, self.Sy)

    def set_gradient_magnitude(self):
        self.G = np.sqrt(np.square(self.Gx) + np.square(self.Gy))

    def sobel(self):
        self.set_gradient_of_x()
        self.set_gradient_of_y()
        self.set_gradient_magnitude()
        return self.thresholding(image=self.G, threshold=self.threshold)

    @staticmethod
    def calculate_convolution(image, mask):
        height, width = image.shape
        k = int((len(mask) - 1) / 2)

        # initialize the result
        out = np.zeros((height, width))

        # rendering
        for i in range(k, height - k):
            for j in range(k, width - k):
                sum = 0
                for m in range(-k, k + 1):
                    for n in range(-k, k + 1):
                        sum = sum + image[i + m][j + n] * mask[k + m][k + n]
                out[i][j] = sum
        return out

    @staticmethod
    def thresholding(image, threshold):
        out = np.copy(image)
        for pixel in np.nditer(out, op_flags=['readwrite']):
            if pixel > threshold:
                pixel[...] = 255
            else:
                pixel[...] = 0
        out = out.astype(np.uint8)
        return out
