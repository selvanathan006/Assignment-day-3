# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d6NtcM0SJoyrNy5amOUY0_WTI9iZI68f

Q.1
"""

import numpy as np
np.arange(2, 50, 3)

"""Q.2"""

# Two list of 5 elements...
m=[1,2,3,4,5]
n=[10,9,8,7,6,]
print("\n",m)
print("\n",n,"\n")
# convert them to numpy arrays and concatenate...
import numpy as np
c=np.array(m+n)
print(c,"\n")
# sort these array....
x = np.array(m+n)
np.sort(x)

"""Q.3"""

import numpy as np
narr=np.arange(16).reshape((4,4))
print(narr)
print("\nsize of nd array:",narr.size)

"""Q.4"""

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
# convert 1d array to 2d array
arr_2d = np.reshape(arr, (2, 5))                        # this program i con't understand the /# np.newaxis, np.expand_dims #/ these ones
print("\n",arr_2d)

"""Q.5"""

import numpy as np
p=np.array([[1,2],[4,5]])
q=np.array([[5,6],[8,9]])
print(p)
print("\n",q)
# vertical stack 
print("\nVstack():\n",np.vstack((p,q)))
# Horizontal stack
print("\nHstack():\n",np.hstack((p,q)))

"""Q.6"""

input_item=["john","smith","william","ingle","anderson","smith","john"]\
# converting our items to  set...
new_set=set(input_item)
print("No of unique items in items:",len(new_set))