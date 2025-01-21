# from numpy import*
# import numpy as np
# # s=array([[1,2,3],[4,5,6]])
# # print(s)
# # k=arange(20)
# # print(k.reshape(2,5,2))
# # print(k.itemsize)
# # l=zeros([2,3],dtype=int)
# # print(l)
# k=array[1,2,3,4,5,6]
# for i in np.nditer(k):
#     print(i)

import numpy as np
#data_array = np.array([[1,2,3],[4,5,6]])
# print(np.transpose(np.array([[1,2,3],[4,5,6]])))
x=np.array(
            [ [3,2,1],
              [5,4,6] ,
              [8,9,7],
              [11,39,37]
              ])
# we can give axis in two ways ,(axis=0 is row,axis=1 is column)
#without axis

#removing row
z=np.delete(x,2,1) #(x--> variable,1--> index of which row or column you want to be deleted 0-->0 is row
print(z)
# #with axis
# print("\n-----------------------\n")
# z=np.delete(x,1,axis=0)
# print(z)

# print("\n-----------------------\n")

# #removing column
# z=np.delete(x,1,1)
# print(z)
# #with axis
# print("\n-----------------------\n")
# z=np.delete(x,1,axis=1)
# print(z)