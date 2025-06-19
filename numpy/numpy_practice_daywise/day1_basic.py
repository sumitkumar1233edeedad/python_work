"""
Day 1: Basic NumPy Practice

Topics:
- Aggregation Functions
- Array Creation Methods

Practice Questions and Example Solutions
"""

import numpy as np

# Question 1: Given a numpy array, find the minimum, maximum, sum, mean, standard deviation, and variance.
arr = np.array([20, 30, 40])
print("Original array:", arr)
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# Question 2: Create a numpy array of random integers and calculate its aggregation statistics.
rand_arr = np.random.randint(1, 100, size=10)
print("\nRandom array:", rand_arr)
print("Min:", np.min(rand_arr))
print("Max:", np.max(rand_arr))
print("Sum:", np.sum(rand_arr))
print("Mean:", np.mean(rand_arr))
print("Std Dev:", np.std(rand_arr))
print("Variance:", np.var(rand_arr))

# Question 3: Given a 2D numpy array, find the row-wise and column-wise sums and means.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", arr_2d)
print("Row-wise sum:", np.sum(arr_2d, axis=1))
print("Column-wise sum:", np.sum(arr_2d, axis=0))
print("Row-wise mean:", np.mean(arr_2d, axis=1))
print("Column-wise mean:", np.mean(arr_2d, axis=0))

# Question 4: Create numpy arrays filled with zeros, ones, and a specific value.
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 4))
full_arr = np.full((2, 2), 7)
print("\nZeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Full array with 7:\n", full_arr)

# Question 5: Generate a sequence of numbers using np.arange with different start, stop, and step values.
seq1 = np.arange(0, 10, 1)
seq2 = np.arange(5, 20, 3)
print("\nSequence 1:", seq1)
print("Sequence 2:", seq2)

# Question 6: Create an identity matrix of a given size.
identity = np.eye(4)
print("\nIdentity matrix:\n", identity)
