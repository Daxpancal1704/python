import numpy as np
# arr1=np.array([1,2,3])
# print(arr1)
# print(np.__version__)
# print(type(arr1))


# "0-D array"


# arr=np.array(12)
# print(arr)

"1-D array"


# D1=np.array([1,2,3,4])
# print(D1)


# "2-D array"

# D2=np.array([[1,2,3,4],[1,2,3,4]])
# print(D2)


"3_D array"

# D3=np.array([[[1,2,3],
#               [1,2,1],
#               [3,4,5],
#               [1,2,3]
#               ]] ,ndmin=10)#ndim-10 uaethe icresin the dimantional
# print(D3)



"ndim check the array is which dimenational"
# print(D3.ndim)

"Check the indexing"
# list=np.array([1,2,3,4])
# print(list[3]+list[0])


"Accessing 2D array [0,1] menas 0 means first row and 1 means column"

list1=np.array([[1,2,3],[2,3,4]])
print(list1[0,1])


import numpy as np
                #"-----block[0]--"        "-----block[1]--"
                #"-----index[0]--"          "#"-----index[1]--""
                #-----0--    ---1----
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])