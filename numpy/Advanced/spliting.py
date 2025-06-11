""" 
np.split
equal

np.hsplit()
np.vsplit()



"""

import numpy as np
arr1 = np.array([1, 2, 3,3, 4,4, 4, 4])
arr2 = np.array([4, 5, 6,3,4,4])

print(np.split(arr2, 2))#(arr is your list and arr  2 is how many time split) [array([4, 5, 6]), array([3, 4, 4])]

print(np.vsplit(arr1.reshape(2, -1), 2))

print(np.hsplit(arr1.reshape(2, -1), 2))