"""
Day 3: Advanced NumPy Practice

Topics:
- Array Manipulation (reshape, flatten, transpose)
- Normalization
- Combining Array Creation and Aggregation

Practice Questions and Example Solutions
"""

import numpy as np

# Question 1: Use numpy functions to manipulate arrays (reshape, flatten, transpose).
arr = np.arange(12)
print("Original array:", arr)
reshaped = arr.reshape((3, 4))
print("Reshaped array (3x4):\n", reshaped)
flattened = reshaped.flatten()
print("Flattened array:", flattened)
transposed = reshaped.T
print("Transposed array:\n", transposed)

# Question 2: Implement a function that normalizes a numpy array using mean and standard deviation.
def normalize_array(a):
    mean = np.mean(a)
    std = np.std(a)
    return (a - mean) / std

arr2 = np.array([10, 20, 30, 40, 50])
print("\nOriginal array:", arr2)
normalized = normalize_array(arr2)
print("Normalized array:", normalized)

# Question 3: Combine array creation and aggregation: create a large array and compute its statistics.
large_arr = np.random.randint(0, 100, size=1000)
print("\nLarge array statistics:")
print("Min:", np.min(large_arr))
print("Max:", np.max(large_arr))
print("Mean:", np.mean(large_arr))
print("Standard Deviation:", np.std(large_arr))
print("Variance:", np.var(large_arr))
