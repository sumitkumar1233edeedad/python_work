import numpy as np

# Create a 2D numpy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)  # Print the original array

# Insert a new row [1, 2, 4] at index 1 (second row) along axis 0 (rows)
# np.insert(array, index, values, axis) inserts values before the given index
new_arr = np.insert(arr, 1, [1, 2, 4], axis=0)
print(new_arr)  # Print the new array with the inserted row