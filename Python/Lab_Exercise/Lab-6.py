                                    # Low Level:
                                    
 # 1. Write a Python program to create the multiplication table (from 1 to 10) of a number

n=int(input("Enter the multiplication table number : "))
print("Multiplication table of ",n)
for i in range(1,10+1):
    print(f"{i} * {n} = {i*n}")

# 2. Write a Python program to print each fruit in a list of fruits using a loop. Assume the list is ["Apple", "Banana", "Cherry"].

fruit=['Apple','Banana','Cherry','Orange','Grapes']
for i in fruit:
    print(i)

# 3. Write a Python program to print all even numbers between 1 and 20 using a loop.

print("The even numbers between 1 to 20 is")
for i in range(1,20+1):
    if i%2==0:
        print(i,end=" ")


# 4. Write a Python program to calculate the factorial of a given number using a loop. Assume the number is 5.

n=int(input("Enter the number to find factorial :"))
k=1
for i in range(1,n+1):
    k*=i
print(f"The factorial of {n} is : {k}")


# 5. Write a Python program to check if a given number is prime using a loop. Assume the number is 29.

n=int(input("Enter the number to find prime  or not :"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(f"{n} is Prime Number..")
else:
    print(f"{n} is Not Prime Number..")


# 6. Write a Python program to count the number of vowels in a given string using a loop. Assume the string is "Artificial Intelligence and Machine Learning".

n=input("Enter the string :").lower()
k=['a','e','i','o','u']
c=0
for i in n:
    if i in k:
        c+=1
print(f"The total numbers of vowels in the string is : {c}")


#.................................................................................................................................................................


                                                        # Medium Level:

# 1. Write a Python program to construct the following pattern, using a nested loop number. 
# Expected Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9

n=int(input("Enter a number of rows : "))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()


# 2.Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n=int(input("Enter a number of rows : "))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()

# 3. Write a Python program to print the alphabet pattern 'D'. 
# Expected Output: 
#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 

n=int(input("Enter a number of rows : "))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1) and (j != 0 and j != n-1):  # Top and bottom sides
            print("*", end="")
        elif (j == 0 or j == n-1) and (i != 0 and i != n-1):  # Left and right sides
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 4.Write a Python program to print the alphabet pattern 'M'. 
# Expected Output: 
#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *

n=int(input("Enter a number of rows : "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1:  # Left and right sides
            print("*", end="")
        elif i == j and i <= n // 2:  # Diagonal from top-left to middle
            print("*", end="")
        elif i + j == n - 1 and i <= n // 2:  # Diagonal from top-right to middle
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 5.Write a Python program to print the alphabet pattern 'O'. 
# Expected Output: 
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

n=int(input("Enter a number of rows : "))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1) and (j != 0 and j != n-1):  
            print("*", end="")
        elif (j == 0 or j == n-1) and (i != 0 and i != n-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 6. Write a Python program to print a right-angled triangle of numbers with n rows. Assume n = 5
# Expected Output :
# 1
# 12
# 123
# 1234
# 12345

n=int(input("Enter a number of rows : "))
for i in range(n+1):
    for j in range(i):
        print(j+1,end="")
    print()

# 7. Write a Python program to print an inverted right-angled triangle of stars with n rows. Assume n = 5
# Expected Output :
# *****
# ****
# ***
# **
# *

n=int(input("Enter a number of rows : "))
for i in range(n+1):
    for j in range(i,n):
        print("*",end="")
    print()

# 8. Write a Python program to print a pyramid of stars with n rows. Assume n = 4.
# Expected Output :
#     *
#    ***
#   *****
#  *******

n=int(input("Enter a number of rows : "))
for i  in range(n):
    for j in range(0,n-i-1):
        print("  ",end="")
    for k in range(0,(2*i)+1):
        print("* ",end="")
    print()

# 9.	Write a Python program to print a diamond pattern of stars with n rows. Assume n = 5.
# Expected Output :
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n=int(input("Enter a number of rows : "))
for i  in range(n):
    for j in range(0,n-i-1):
        print("  ",end="")
    for k in range(0,(2*i)+1):
        print("* ",end="")
    print()
for i  in range(n-2,-1,-1):
    for j in range(0,n-i-1):
        print("  ",end="")
    for k in range(0,(2*i)+1):
        print("* ",end="")
    print()


# 10. Write a Python program to print a right-angled triangle of incrementing numbers with n rows. Assume n = 5.
# Expected Output :
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

n=int(input("Enter a number of rows : "))
k=1
for i in range(n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

#...........................................................................................................................................................
                                #High Level

# 1. Write a Python program to check the validity of passwords input by users. 
# Validation : 
# At least 1 letter between [a-z] and 1 letter between [A-Z]. 
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

p=input("Enter your password for check :")
s,h,o=0,0,0
sy=['$','#','@']
s1=len(p)
if s1>6 and s1<=16:
    for i in p:
        if i.isalpha():
            s+=1
        if i.isdigit():
            h+=1
        if i in sy:
            o+=1
    if s>0 and h>0 and o>0:
        print("Valid Password..")
    elif s==0:
        print("Give atleast 1 upper and lower case..")
    elif h==0:
        print("Give atleasr 1 number...")
    elif o==0:
        print("Give atleast 1 special character ($,#,@)..")
    else:
        pass
else:
    print("Your password must be in range of 6-16 characters...")