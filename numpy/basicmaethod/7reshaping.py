"""
NumPy Array Reshaping Tutorial

This script demonstrates:
1. Creating a 1D NumPy array.
2. Reshaping it into a 2D array.
3. Flattening the 2D array back to 1D using ravel() and flatten().
    - ravel(): Returns a flattened view (changes affect the original if possible).
    - flatten(): Returns a flattened copy (changes do not affect the original).
"""

import numpy as np

# Step 1: Create a 1D numpy array with 9 elements
arr = np.array([1, 2, 4, 5, 6, 7, 8, 9, 10])
print("Original 1D array:", arr)

# Step 2: Reshape the array to 3 rows and 3 columns (2D array)
reshaped_arr = arr.reshape(3, 3)
print("\nReshaped to 3x3 array:\n", reshaped_arr)

# Step 3: Flatten the 2D array back to 1D
ravel_arr = reshaped_arr.ravel()    # Returns a view
flatten_arr = reshaped_arr.flatten() # Returns a copy

print("\nFlattened array using ravel():", ravel_arr)
print("Flattened array using flatten():", flatten_arr)

# Demonstrate the difference between ravel() and flatten()
ravel_arr[0] = 100
print("\nAfter modifying ravel_arr[0]:")
print("reshaped_arr:\n", reshaped_arr)
print("flatten_arr (unchanged):", flatten_arr)
