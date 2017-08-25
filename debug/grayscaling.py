import cv2


def convert_brg2gray():
    # Load input image
    image = cv2.imread('../images/image.jpg')

    # Use 'cvtColor' to convert to gray color
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray image', gray_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def convert_brg2hvs():
    # Load input image
    image = cv2.imread('../images/image.jpg')

    # Use 'cvtColor' to convert to hvs color
    hvs_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('gray image', hvs_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def convert_brg2red():
    # Load input image
    image = cv2.imread('../images/image.jpg')

    red_image = []
    for row in image:
        for cell in row:
            cell = cell[:1]

    # Use 'cvtColor' to convert to hvs color
    hvs_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('gray image', hvs_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


convert_brg2gray()
