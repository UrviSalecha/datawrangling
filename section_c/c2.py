import pandas as pd
import numpy as np
import seaborn as sns

sales=pd.DataFrame({
    'order_date':['2026-01-05','2026-01-18','2026-02-02',
                  '2026-02-14','2026-03-01','2026-03-20'],
    'region':[' North','south','North ','East','SOUTH','east'],
    'product':['Pen','Notebook','Pen','Bag','Bag','Notebook'],
    'units':[10,5,np.nan,2,4,8],
    'prices':[20,60,20,500,500,60],
    'rep':['Ravi','Sita','Ravi','Kiran','Sita','Kiran']
})
# clean region 
# extra spaces remove
sales['region']=sales['region'].str.strip()
print(sales)
print(sales['units'].fillna(sales['units'].median(),inplace=True))

# new column revenue convert order_date to datetime and add a month column month name
sales['revenue']=sales['units']*sales['prices']
sales['order_date']=pd.to_datetime(sales['order_date'])
sales['month']=sales['order_date'].dt.month_name()
print(sales.head())

# highest revenue per region sorted high first
print(sales.groupby('region')['revenue'].sum().sort_values(ascending=False))
# output: region
# SOUTH    2000.0
# East     1000.0
# east      480.0
# North     300.0
# south     300.0
# Name: revenue, dtype: float64


# pivot table rows=region columns=product values=total_revenue missing =0 
# seaborn bar plot of revenue by region
pivot_table=sales.pivot_table(index='region',columns='product',values='revenue',aggfunc='sum',fill_value=0)
print(pivot_table)
#seaborn bar plot of revenue by region
sns.barplot(x='region',y='revenue',data=sales)