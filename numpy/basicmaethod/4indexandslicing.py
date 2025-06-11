import numpy as np

"""This script demonstrates the use of NumPy for
numerical computations and indexing.
"""


# Create a sample NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Basic indexing
print("Element at index 0:", arr[0])

# Slicing
print("Elements from index 1 to 3 (step 1):", arr[1:4:1])
print("Elements from index 0 to 4 (step 2):", arr[0:5:2])

# Negative indexing
print("Last element:", arr[-1])

# Multi-dimensional indexing
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at row 1, column 2:", matrix[1, 2])
 
# Boolean indexing
print("Elements greater than 25:", arr[arr > 25])

# Fancy indexing
print("Fancy indexing with list of indices [0, 2, 4]:", arr[[0, 2, 4]])
print("Fancy indexing with array of indices [1, 3]:", arr[np.array([1, 3])])

# Fancy indexing on multi-dimensional array
print("Fancy indexing on matrix rows 0 and 1, columns 1 and 2:")
print(matrix[[0, 1], [1, 2]])
