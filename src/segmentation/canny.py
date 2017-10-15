# Author: KhanhLQ

import cv2
import numpy as np
import scipy

from __utils__.general import show_image, pickle_dump_object, pickle_load_object
from sobel import calculate_gradient_magnitude, threshold


def canny_open_cv(image, lower=None, upper=None):
    mean = image.mean()
    if lower is None:
        lower = int(mean - mean * 0.25)
    if upper is None:
        upper = int(mean + mean * 0.25)
    edges = cv2.Canny(image, threshold1=lower, threshold2=upper)
    return edges


image = cv2.imread("../../images/elena.jpg", 0)

# pickle_dump_object(gradient_magitude, "elena_gradient_mag.pickle")
gradient_magitude = pickle_load_object("elena_gradient_mag.pickle")


# show_image(threshold(gradient_magitude, 100))

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
    correlate = scipy.ndimage.correlate
    correlate1d = scipy.ndimage.correlate1d
    convolve = scipy.ndimage.convolve
    convolve1d = scipy.ndimage.convolve1d

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


res = non_maximal_suppression(gradient_magitude)
pass
# edges = canny_open_cv(image)
# show_image(np.hstack((image, edges)))
