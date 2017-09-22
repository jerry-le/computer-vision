import cv2
import numpy as np

from __utils__.general import show_image


def scaling_neighbor(image, scale=1):
    height = image.shape[0]
    width = image.shape[1]

    dest_height = int(height * scale)
    dest_width = int(width * scale)

    out = np.zeros(shape=(dest_height, dest_width), dtype=np.uint8)

    for x in range(0, dest_height - 1):
        for y in range(0, dest_width - 1):
            x_dest = x
            y_dest = y
            float_x = x_dest / scale
            float_y = y_dest / scale
            x_source = int(float_x + 0.5)
            y_source = int(float_y + 0.5)
            out[x][y] = image[x_source][y_source]
    return out


def scaling_linear(image, scale=1):
    height = image.shape[0]
    width = image.shape[1]

    dest_height = int(height * scale)
    dest_width = int(width * scale)

    out = np.zeros(shape=(dest_height, dest_width), dtype=np.uint8)
    for x in range(0, dest_height - 1):
        for y in range(0, dest_width - 1):

            pass
    return out

def bilinear_interpolate(im, x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    x0 = np.clip(x0, 0, im.shape[1]-1)
    x1 = np.clip(x1, 0, im.shape[1]-1)
    y0 = np.clip(y0, 0, im.shape[0]-1)
    y1 = np.clip(y1, 0, im.shape[0]-1)

    Ia = im[y0, x0]
    Ib = im[y1, x0]
    Ic = im[y0, x1]
    Id = im[y1, x1]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    return wa*Ia + wb*Ib + wc*Ic + wd*Id


image = cv2.imread('../../images/shape.png', 0)
scale = 2
# out = scaling_neighbor(image, scale=scale)
out = bilinear_interpolate(image, 1, 1)
show_image(out, name='output')
show_image(image, name='input')
