import pandas as pd
import numpy as np

sales=pd.DataFrame({
    'order_date':['2026-01-05','2026-01-18','2026-02-02',
                  '2026-02-14','2026-03-01','2026-03-20'],
    'region':['North','south','North','East','SOUTH','east'],
    'product':['Pen','Notebook','Pen','Bag','Bag','Notebook'],
    'units':[10,5,np.nan,2,4,8],
    'prices':[20,60,20,500,500,60],
    'rep':['Ravi','Sita','Ravi','Kiran','Sita','Kiran']
})
print(sales.isnull().sum().sum()) # output: 1
print(sales.dropna().shape) #output: (5, 6)
#missing units value with median of units
# print(sales['units'].fillna(sales['units'].median(),inplace=True)) # output: None
# print(sales.loc[0:3])
print(sales.groupby('rep')['units'].sum())