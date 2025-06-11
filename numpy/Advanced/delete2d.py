import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 3, 4 ],
               [2, 4, 5],
               [6, 7, 8]])

# Delete the first row (index 0) from the array
arrn = np.delete(arr, 0, axis=0)

# Print the resulting array
print(arrn)