import numpy as np

a=np.array([[10,20,30],[40,50,60]])
 # mean of each column and output
print(np.mean(a,axis=0))
print(a[a>25])
#outputs: i)[25. 35. 45.] and ii)[30 40 50 60]
print(np.arange(2,11,3))