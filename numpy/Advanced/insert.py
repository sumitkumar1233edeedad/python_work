""" 
insert method :->
np.insert(array, index, value, asix = none)
index-
value-
axis-
2d matrix
axis is zero  = 0 row_wise
axis is 1 = 1 column_wise
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 7])
print(arr)
new_arr = np.insert(arr, 3, 10, axis=0)
print(new_arr)