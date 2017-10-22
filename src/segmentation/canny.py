# Author: KhanhLQ

from segmentation.sobel import SobelDetectionEdge
from __utils__.general import pickle_load_object, show_image
from scipy import ndimage
import numpy as np
import scipy
import math


class CannyEdgeDetection:
    def __init__(self, img, gradient_x=None, gradient_y=None, gradient=None):
        self.img = img
        self.gradient_magnitude_of_x = gradient_x
        self.gradient_magnitude_of_y = gradient_y
        self.gradient_magnitude = gradient
        self.theta = None
        if self.gradient_magnitude is None:
            self.compute_gradient()
        self.compute_theta()

    def compute_gradient(self):
        sobel = SobelDetectionEdge(img=self.img)
        self.gradient_magnitude_of_x = sobel.get_gradient_of_x()
        self.gradient_magnitude_of_y = sobel.get_gradient_of_y()
        self.gradient_magnitude = sobel.get_gradient_magnitude()

    def compute_theta(self):
        try:
            # self.theta = self.gradient_magnitude_of_y / self.gradient_magnitude_of_x
            # for pixel in np.nditer(self.theta, op_flags=['readwrite']):
            #     if math.isnan(pixel):
            #         pixel[...] = 0
            #     if math.isinf(pixel):
            #         pixel[...] = 10
            self.theta = np.arctan2(self.gradient_magnitude_of_y, self.gradient_magnitude_of_x)
        except Exception as e:
            pass

    def canny(self):
        self.non_maximal_suppression(self.gradient_magnitude, self.theta)
        pass

    @staticmethod
    def non_maximal_suppression(G, theta):
        """
            Performs non-maximal-suppression of gradients.
            Bins into 4 directions (up/down, left/right, both diagonals),
            and sets non-maximal elements in a 3x3 neighborhood to zero.
            Args:
                G: A (height, width) float numpy array of gradient magnitudes.
                theta: A (height, width) float numpy array of gradient directions.
            Returns:
                suppressed: A (height, width) float numpy array of suppressed
                    gradient magnitudes.
        """

        theta *= 180.0 / np.pi
        theta[theta > 180.0] -= 180.0
        hits = np.zeros_like(G, dtype=bool)
        correlate = ndimage.correlate
        correlate1d = ndimage.correlate1d
        convolve = ndimage.convolve
        convolve1d = ndimage.convolve1d

        kernel = np.array([0.0, 1.0, -1.0])
        mask = np.logical_or(theta < 22.5, theta > 157.5)
        hits[mask] = np.logical_and(correlate1d(G, kernel, axis=-1)[mask] >= 0.0,
                                    convolve1d(G, kernel, axis=-1)[mask] >= 0.0)

        mask = np.logical_and(theta >= 67.5, theta < 112.5)
        hits[mask] = np.logical_and(correlate1d(G, kernel, axis=0)[mask] >= 0.0,
                                    convolve1d(G, kernel, axis=0)[mask] >= 0.0)

        kernel = np.array([[0.0, 0.0, 0.0],
                           [0.0, 1.0, 0.0],
                           [0.0, 0.0, -1.0]])
        mask = np.logical_and(theta >= 22.5, theta < 67.5)
        hits[mask] = np.logical_and(correlate(G, kernel)[mask] >= 0.0,
                                    convolve(G, kernel)[mask] >= 0.0)

        kernel = np.array([[0.0, 0.0, 0.0],
                           [0.0, 1.0, 0.0],
                           [-1.0, 0.0, 0.0]])
        mask = np.logical_and(theta >= 112.5, theta < 157.5)
        hits[mask] = np.logical_and(correlate(G, kernel)[mask] >= 0.0,
                                    convolve(G, kernel)[mask] >= 0.0)

        suppressed = G.copy()
        suppressed[np.logical_not(hits)] = 0.0

        return suppressed

    @staticmethod
    def double_thresholding(img, high, low):
        out = np.copy(img)
        height, width = img.shape

        # if a pixel value greater than high threshold, it is strong edge
        strong_edges = (out > high)

        # strong edges is 2, weak edges is 1, non-edge is zero
        threshold_edges = np.array(strong_edges.astype(np.uint8)) + (out > low)

        for r in range(0, height - 1):
            for c in range(0, width - 1):
                if threshold_edges[r][c] != 1:
                    continue # not the weak edge

                # patch 3x3 surrounding current pixel
                local_patch = threshold_edges[r - 1: r + 2, c - 1: c + 2]
                patch_max = np.max(local_patch)
                if patch_max == 2:
                    threshold_edges[r][c] = 2
                else:
                    threshold_edges[r][c] = 0

        # fit image dtype
        max_value = np.iinfo(threshold_edges.dtype).max
        threshold_edges[threshold_edges > 0] = max_value
        return threshold_edges
