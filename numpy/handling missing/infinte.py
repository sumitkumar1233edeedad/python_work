''' 
np.isinf() 10*1000

1/0

'''

import numpy as np

ar = np.array([10, 20, 30, np.inf, -4 , -np.inf, 60])

print(ar)#without function

print(np.isinf(ar))#with function