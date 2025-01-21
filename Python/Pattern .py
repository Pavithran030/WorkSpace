"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""


# n=int(input("Enter a number of rows : "))
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

"""
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
"""

# for i in range(n+1):
#     for j in range(n):
#         if j<=n-i-1:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(n+1):
#     for j in range(n):
#         if j<=i:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""
n=int(40)

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


# for i in range(n+1):
#     for j in range(n):
#         if j<=n-i-1:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     for j in range(i-1):
#         print("*",end=" ")
#     print()

