import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

region_units=pd.DataFrame({'region':['North','South','East'],
                           'units':[15,9,10]})


plot=region_units.plot.bar(x='region',y='units',color='yellow',title='Units Sold by Region')
print(plot)