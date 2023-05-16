import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis=0):
    array1 = array1.squeeze()
    array2 = array2.squeeze()

    for i in range(array1.ndim):
        if i != axis:
            if array1.shape[i] != array2.shape[i]:
                raise ValueError("axes are not matching!")

    for i in range(array2.ndim):
        if i != axis:
            if array1.shape[i] != array2.shape[i]:
                raise ValueError("axes are not matching!")

    concatenated = np.concatenate([array1, array2], axis)
    return concatenated

    


if __name__ == "__main__":
    # use this for your own testing!

    pass
