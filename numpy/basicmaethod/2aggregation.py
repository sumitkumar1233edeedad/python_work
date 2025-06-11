""" 
This module demonstrates various aggregation methods using NumPy arrays.
Aggregation methods included:
1. Finding the maximum element in the array.
2. Finding the minimum element in the array.
3. Calculating the sum of all elements in the array.
4. Calculating the mean (average) of the array elements.
5. Calculating the standard deviation of the array elements.
6. Calculating the product of all elements in the array.
Each method showcases how to perform basic aggregation operations on NumPy arrays.
 
"""
import numpy as np

# Create a NumPy array
arr = np.array([20, 30 , 40])

# Display the original array
print("Original array: ", arr)

# Find and print the minimum value in the array
print('min', np.min(arr))

# Find and print the maximum value in the array
print('max', np.max(arr))

# Calculate and print the sum of all elements
print('sum', np.sum(arr))

# Calculate and print the mean (average) of the elements
print('mean average', np.mean(arr))

# Calculate and print the standard deviation of the elements
print('std deviation', np.std(arr))

# Calculate and print the variance of the elements
print('var product of element ', np.var(arr))