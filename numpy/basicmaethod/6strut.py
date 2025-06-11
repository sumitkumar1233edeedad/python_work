"""
   method :->
   > shape : this how much dimension check
   > size : total number of array
   > ndim : show the dimension
   > .dtype : check datatype hold array
   > astype() : change datatype of array
    """
import numpy as np
# Create a 2D numpy array with shape (2, 3)
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([[2, 3, 4],
                 [2, 3, 4]])
arr_3 = np.array([[[2, 3, 4],
                 [2, 3, 4],
                 [2, 3, 4]]])
# Print the shape of the array
print("shape method",arr_2.shape)


print("size array", arr_2.size)


print('ndim array ',arr_3.ndim, arr_2.ndim, arr_1.ndim)


print(".dtype check ", arr_2.dtype)


change = arr_2.astype(str)
print("astype convert ", change)