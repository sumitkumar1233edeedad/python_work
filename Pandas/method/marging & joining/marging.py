import pandas as pd

df_coutomer = pd.DataFrame({
    "customer_id":[1, 2, 4],
    'name' : ['ram', 'suresh', 'ramesh'],
    
})
#order data frame

df_orders = pd.DataFrame({
    'customer_id':[1, 2, 3],
    'order_amount': [230, 200, 500]
})

df_merged = pd.merge(df_coutomer, df_orders, on = 'customer_id', how = 'right')
print('inner join')
# join method  inner , outer, left, right
print(df_merged)