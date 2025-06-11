''' 
np.nan_to_num(array , nan=value) default = 0

'''

import numpy as np

ar = np.array([10, 20, 30, np.nan, 80, np.nan])

clear_ar = np.nan_to_num(ar, nan = 100)#first is arr name , second is any number you want change but you want be not change than default value auto 0 put on

print(clear_ar)