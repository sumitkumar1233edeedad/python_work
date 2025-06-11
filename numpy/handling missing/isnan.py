"""
Study Notes:

- np.isnan(array): This function checks element-wise for NaN (Not a Number) values in a NumPy array.
- Returns a boolean array of the same shape as input, where True indicates the presence of NaN.
- NaN is a special floating-point value defined by the IEEE 754 standard.
- NaN is not equal to itself: np.nan == np.nan returns False.
- Useful for data cleaning and preprocessing to identify or filter out missing values.

Example:
    arr = np.array([1, 2, np.nan])
    np.isnan(arr)  # Output: [False False  True]
"""
import numpy as np

# Create a NumPy array with some NaN values
arr = np.array([1, 2, 4, np.nan , 5, np.nan, 6])

# Check which elements are NaN
print(np.isnan(arr))

# Demonstrate that NaN is not equal to itself
print(np.nan == np.nan)