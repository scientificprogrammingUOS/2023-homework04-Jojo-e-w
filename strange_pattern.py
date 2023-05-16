import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    # delete the NotImplementedError when you write your function.
    (m, n) = shape
    array = np.full(shape, False, dtype=bool)

    array[0:m+1:3, 0:n+1:3] = True
    array[1:m+1:3, 2:n+1:3] = True
    array[2:m+1:3, 1:n+1:3] = True

    return array

if __name__ == "__main__":
    # use this for your own testing!

    pass
