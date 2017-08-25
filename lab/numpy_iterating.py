import numpy as np

def single_array_iteration():
    # Single array iteration
    a = np.arange(6).reshape(2,3)
    for x in np.nditer(a):
        print x,

    print
    for x in np.nditer(a, order='F'):
        print x,

    print
    for x in np.nditer(a, order='C'):
        print x,


def modify_array_value():
    a = np.arange(6).reshape(2,3)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2 * x
    print a

modify_array_value()



