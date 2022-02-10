import numpy as np
array1=np.array([1,2,3,4,5,6,7,8,9,10])

array=np.array([1,2,3,4,5,6,7,8,9,10]) # numbers from 0 to 9

a=np.ones((3,3),true,dtype=bool)
print(a)

slice=np.array([1,2,3,4,5,6,7,8,9])
print(slice[3:9:2*n+1])


array=np.array([1,2,3,4,5,6,7,8,9,10])
print(array)

bool_arr = np.ones((3,3), dtype=bool)
print(bool_arr)

x = np.arange(3, 10, 2)
print(x)

def v1():
  v1=np.arange(1, 10, 1) 
  v1[v1%2==1]*=-1    # select and multiply only odd indexes 
  print(v1)
# Alternatively
import numpy as np 
arr=np.arange(1,10)
arr[1::2]-1

import numpy as np
a=np.arange(1,3).reshape(2,1)
print(a)


import numpy as np
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
np.hstack((a,b))
print(np.vstack((a,b)))

a = np.array([[1], [2], [3]])       # 1D array created 
b = np.array([[4], [5], [6]])
np.vstack((a,b))                    # a and b stacked 
a=np.arange(1,7).reshape(2,3)      # reshaped into 2x3 dimension 
c=np.dot(a,b)                  
print(c)
e=np.sum(c,axis =1)                # axis =1 is column direction    
print(e)




 



