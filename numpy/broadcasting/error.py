import numpy as np

# Create a 2x4 array
arr = np.array([[1, 3, 4, 5], [2, 5, 6, 6]])

# Create a 1D array with 2 elements
arr1 = np.array([2, 3])

# This will raise a ValueError due to incompatible shapes for broadcasting
try:
    rs = arr + arr1
    print("Result of arr + arr1:\n", rs)
    
except ValueError as e:
    print("Error:", e)