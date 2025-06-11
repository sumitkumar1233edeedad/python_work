# Concatenate two arrays using numpy's concatenate function
# Syntax: np.concatenate((arr1, arr2), axis=0)

import numpy as np

# Create two numpy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([5, 6, 7])

# Concatenate arr1 and arr2 along axis 0 (default for 1D arrays)
arr3 = np.concatenate((arr1, arr2))
print(arr3)