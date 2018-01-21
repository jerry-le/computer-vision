# Author: KhanhLQ

import cv2
import numpy as np
from __utils__.general import show_image


def histeq(img, nbr_bins=256):
    # Get image histogram
    imhist, bins = np.histogram(img.ravel(), 256, [0, 256])

    # Calculate cumsum of intensives
    cdf = imhist.cumsum()

    # Look up table
    lut = 255 * cdf / cdf[-1]

    # Use linear interpolation of cdf to find new pixel values
    im2 = np.interp(img.ravel(), bins[:-1], lut)

    return im2.reshape(img.shape), lut


def histspec(imsrc, imtint):
    nbr_bins = 255
    if len(imsrc.shape) < 3:
        imsrc = imsrc[:, :, np.newaxis]
        imtint = imtint[:, :, np.newaxis]

    imres = imsrc.copy()
    for d in range(imsrc.shape[2]):
        imhist, bins = np.histogram(imsrc[:, :, d].flatten(), nbr_bins, normed=True)
        tinthist, bins = np.histogram(imtint[:, :, d].flatten(), nbr_bins, normed=True)

        cdfsrc = imhist.cumsum()  # cumulative distribution function
        cdfsrc = (255 * cdfsrc / cdfsrc[-1]).astype(np.uint8)  # normalize

        cdftint = tinthist.cumsum()  # cumulative distribution function
        cdftint = (255 * cdftint / cdftint[-1]).astype(np.uint8)  # normalize

        im2 = np.interp(imsrc[:, :, d].flatten(), bins[:-1], cdfsrc)

        im3 = np.interp(im2, cdftint, bins[:-1])

        imres[:, :, d] = im3.reshape((imsrc.shape[0], imsrc.shape[1]))

    return imres


if __name__ == '__main__':
    # img_path = '../../asserts/images/elena.jpg'
    # img = cv2.imread(img_path, 0)
    # imres, lut = histeq(img)
    # imres = imres.astype(np.uint8)
    # show_image(np.hstack((img, imres)))

    src_path = '../../asserts/images/building.png'
    tint_path = '../../asserts/images/building2.png'
    imsrc = cv2.imread(src_path)
    imtint = cv2.imread(tint_path)
    imres = histspec(imsrc, imtint)
    show_image(np.hstack((imsrc, imres)))
