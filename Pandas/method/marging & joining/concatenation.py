'''
vertically (row)
horizontally (columns)

pd.concate([df1, df2], axis = 0 ignore_index= True)


'''

import pandas as pd
#vertically
df_region1 = pd.DataFrame({
    'customerid':[1, 2],
    'name':['ram', 'kumar']
})

df_region2 = pd.DataFrame({
    'customerid':[3, 4],
    'name':['ramu', 'bachu']
})

df_con = pd.concat([df_region1, df_region2], ignore_index=True)
print(df_con)

print('horizontally')
#horizontally
df_con1 = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_con1)