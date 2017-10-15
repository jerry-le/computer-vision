import cv2
import pickle


def show_image(image, name='Image'):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def pickle_dump_object(obj, filename=None):
    # type: (object, object) -> object
    with open(filename, 'w') as f:  # Python 3: open(..., 'wb')
        pickle.dump(obj, f)


def pickle_load_object(filename=None):
    with open(filename) as f:  # Python 3: open(..., 'rb')
        obj = pickle.load(f)
    return obj
