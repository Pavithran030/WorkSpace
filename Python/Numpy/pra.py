# import numpy as np
# arr = np.arange(5)
# indices_to_keep = [0, 1, 2, 3]
# new_arr = arr[indices_to_keep]
# print(np.delete(arr,-1))

# import numpy as np
# data = np.array([10, 7, 4, 3, 2, 1,6])
# median_value = np.median(data)
# print(f"Median: {median_value:.2f}")
# print(np.shape(data))

# import numpy as np

# # Create a sample 2D array
# nums = np.array([[1, 2, 3, 4],
#                  [0, 1, 3, 4],
#                  [90, 91, 93, 94],
#                  [5, 0, 3, 2]])

# # Swap rows and columns in reverse order
# new_nums = nums[::-1, ::-1]

# # Print the original and modified arrays
# print("Original array:")
# print(nums)
# print("\nSwap rows and columns of the array in reverse order:")
# print(new_nums)
# import numpy as np
# def moving_average(arr,n):
#     if n<=0 and n>len(arr):
#         raise ValueError("invalid value of n.")
#     move=np.zeros(len(prices)-n+1)
#     for i in range(len(move)):
#         tot=0
#         for j in range(n):
#             tot+=arr[i+j]
#         move[i]=tot/n
#     return move
# prices=[int(input("Enter the prices: \n")) for i in range(5)]
# n=int(input("Enter no. of days : \n"))
# print (f"moving average of the stock prices of {n}-days is: {moving_average (prices,n)}")


import numpy as np

def convert_to_grayscale(rgb):
    h,w,_=rgb.shape
    gray=np.zeros((h,w), dtype=rgb.dtype)
    for i in range(h):
        for j in range(w):
            r,g,b=rgb[i,j]
            gray[i,j]=0.2989*r+0.5870*g+0.1140*b
    return gray
colour=np.array([[[255,0,0], [0,255,0], [0,0,255]], [[255,255,0], [255,0,255], [0,255,255]], [[0,255,255], [255,0,255], [255,255,0]]])
print(f"the gray image: \n{convert_to_grayscale(colour)}")