""" 
np.delete()

np.delete(arr, obj, axis=None)

"""

import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3])

# Delete the element at index 2 (third element) along axis 0
arrn = np.delete(arr, 2, axis=0)

# Print the resulting array
print(arrn)