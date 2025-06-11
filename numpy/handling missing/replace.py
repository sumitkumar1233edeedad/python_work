# Study Notes:
"""
This script demonstrates handling of infinite values in NumPy arrays.
Key Features:
- Shows how to represent positive and negative infinity using `np.inf` and `-np.inf`.
- Utilizes `np.isinf()` to identify infinite values within a NumPy array.
- Demonstrates the use of `np.nan_to_num()` to replace positive infinity (`np.inf`) and negative infinity (`-np.inf`) with specified finite values.
- Useful for preprocessing and cleaning data before analysis or machine learning tasks.
Steps:
1. Creates a NumPy array containing finite and infinite values.
2. Prints the original array.
3. Prints a boolean array indicating the positions of infinite values.
4. Replaces infinite values with user-defined finite numbers and prints the result.
"""
# - np.inf and -np.inf represent positive and negative infinity in numpy arrays.
# - np.isinf(array) returns a boolean array indicating where the values are infinite.
# - np.nan_to_num(array, posinf=..., neginf=...) replaces inf/-inf with specified values.
# - Useful for cleaning data before analysis or machine learning.
import numpy as np

ar = np.array([1, 2, 3, np.inf, -4 , -np.inf, 6])

print(ar)#without function

print(np.isinf(ar))#with function


create_var =np.nan_to_num(ar, posinf = 1000, neginf=-1000)
print(create_var)