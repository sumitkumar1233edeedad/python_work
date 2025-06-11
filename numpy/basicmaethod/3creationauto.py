#creation of array for  like that auto fill out array like zero or one
import numpy as np
"""
        auto array creation example:->
        > one and zero
        > default value 
        > sequences arr 
        >identity matrices
    """
#zero array auto
zero = np.zeros((2,3))

#one array auto
one = np.ones((2,3))

#fill array default value
fill = np.full((2, 4),7)

#arrange function
arr = np.arange(1, 10, 2) 

#identity matrix eye(size)
identity = np.eye(5)


print("first array  is auto fill zero :->  \n", zero)
print("second array is auto fill one :-> \n", one)
print("third array is auto fill defaults value :-> \n", fill)
print("fourth array is auto fill arrange :-> \n", arr)
print("fifth array is auto fill identity matrix :->\n",identity)
