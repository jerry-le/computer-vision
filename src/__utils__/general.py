import cv2


def show_image(image, name='Image'):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()