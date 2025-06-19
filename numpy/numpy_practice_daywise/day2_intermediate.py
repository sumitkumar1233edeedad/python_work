"""
Day 2: Intermediate NumPy Practice

Topics:
- Element-wise Mathematical Operations
- Broadcasting Rules

Practice Questions and Example Solutions
"""

import numpy as np

# Question 1: Perform element-wise addition, multiplication, and exponentiation on numpy arrays.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array a:", a)
print("Array b:", b)
print("Element-wise addition:", a + b)
print("Element-wise multiplication:", a * b)
print("Element-wise exponentiation (a^b):", a ** b)

# Question 2: Given two numpy arrays, perform element-wise operations and explain broadcasting rules.
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([1, 0, 1])
print("\nArray x:\n", x)
print("Array y:", y)
print("Element-wise addition with broadcasting:", x + y)
print("Explanation: y is broadcasted to match the shape of x for element-wise addition.")

# Question 3: Write code to apply a mathematical function (e.g., square, square root) element-wise on a numpy array.
arr = np.array([1, 4, 9, 16])
print("\nOriginal array:", arr)
print("Square of elements:", np.square(arr))
print("Square root of elements:", np.sqrt(arr))

# Question 4: Explore numpy's random module to generate arrays and compute their properties.
rand_arr = np.random.rand(5)
print("\nRandom array with values between 0 and 1:", rand_arr)
print("Mean of random array:", np.mean(rand_arr))
print("Standard deviation of random array:", np.std(rand_arr))
