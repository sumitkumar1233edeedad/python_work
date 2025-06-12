import pandas as pd

data = {
    'time':[1, 2, 3, 4, 5],
    'value':[10, None, 30, 40, 50]
}

df = pd.DataFrame(data)
print('before data interpolation')
print(df)
df['value'] = df['value'].interpolate(method='linear')
print('after data interpolation')
print(df)

'''
1 timer series data
2 - numeric data with trends
3- avoid dropping rows
'''