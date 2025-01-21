## Using recursion design a program to solve tower of honoi(honoi is one type of algorithm)

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N = 3

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# Contributed By Harshit Agrawal

#################################################################################################################################################

# 11)Suppose you are working on a project that involves analyzing data collected from various sensors deployed in a smart city The data collected is organized into matrices where each row represents a sensor reading at a specific time, and each column represents a different sensor. Your task is to transpose these matrices to reorganize the data for further analysis and visualization.

from numpy import *

def Transpose_matrix(org):
    row,col=org.shape
    trans=zeros((row,col),dtype=org.dtype)

    for i in range(row):
        for j in range(col):
            trans[i][j]=org[j][i]

    print(f" the given matrix :\n{trans}\n")

x=np.array(
            [ [1,2,3],
              [4,5,6] ,
              [7,8,9],
            ])

print(f"the transpose the given matrix :\n{x}\n ")
Transpose_matrix(x)

#################################################################################################################################################

#12). Your task is to extract specific information from the student performance dataset using slicing and advanced indexing techniques in NumPy. This involves extracting data for a particular student, specific subjects, and data for students meeting certain criteria.

from numpy import*

student_performance = array([
    [70, 80, 90, 85,85],  # Student 0
    [60, 75, 80, 70,98],  # Student 1
    [85, 90, 95, 92,94],  # Student 2
    [50, 65, 70, 60,65],  # Student 3
    [98, 85, 80, 87,90]   # Student 4
])

# for specific student.

lst=['tamil','english','maths','science','social']

x=int(input("Enter the student number(0-4) :"))

print("\nsubject :\ntamil   -0\nenglish -1\nmaths   -2\nscience -3\nsocial  -4\n")

y=int(input("Enter the start subject number : "))
z=int(input("Enter the end subject number : "))

perf=student_performance[x,y:z+1]
l=lst[y:z+1]
print(f"the performance of student {x} for the subjects  :\n")
for i in range(len(perf)):
    print(f"{l[i]} : {perf[i]}\n")

#data for students meeting certain criteria.

certain_criteria=student_performance[(student_performance>80).all(axis=1)]
print("\nStudents meeting criteria (score above 80 in all subjects):")
r,c=where(student_performance==certain_criteria)
print(f"student {r[0]}")

#################################################################################################################################################


# 13). Alice is a data analyst working on a project where she needs to perform statistical analysis on a dataset. She needs to create an array of even integers ranging from 30 to 70 to use as indices for filtering out specific data points from the dataset. To efficiently generate this array, she decides to use NumPy, a powerful numerical computing library in Python.
from numpy import *

x=arange(30,71,2)
print("the array of even integers ranging from 30 to 70 :\n")
print(x)

#################################################################################################################################################

# 14). Bob is a researcher in a laboratory where they frequently deal with linear transformations and operations in their experiments. As part of his current project, Bob needs to perform matrix operations where he requires a 3x3 identity matrix. Since creating an identity matrix manually can be tedious and prone to errors, Bob decides to use NumPy, a powerful numerical computing library in Python.
# identity matrix
from numpy import *
iden=zeros([3,3],dtype=int32)
for i in range(3):
  iden[i][i]=1
print("the identity matrix : \n")
print(iden)


#################################################################################################################################################3


# part - C

# 15). Sarah is developing a Python program that involves user input for numerical values. In a specific part of her program, she needs the user to input an integer. However, Sarah wants to ensure that the program handles cases where the user might input a non-integer value, such as a string or a floating-point number. To achieve this, she implements a validation mechanism that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

while True :
  try :
    x=int(input("Enter an integer : "))
    print(f"Thank you, you entered the integer : {x}.")
    break
  except ValueError as e:
    print("Error : ",e)



# 16.You are a teacher who keeps a daily log of student attendance and class notes. Each day, you append the attendance and notes to a file named "class_log.txt". At the end of each day, you want to review what has been logged

f=open("class_log.txt","a+")
print("student attenance :")
p=0
a=0

print("present - p \nabsent  - a")
try :
    z=int(input("Enter the total no. of students :"))
except ValueError as e:
    print("Error ",e)

for i in range(1,z+1):
    x=input(f"Roll.no.{i} : ")
    if x=='p' or x== 'P':
        p+=1
    elif x=="a" or x== "A":
        a+=1
    else:
        print("invalid input")

a=f"\nthe total no. of students :{str(z)},no. of students present :{str(p)},no. of students absent :{str(a)}\n"
print(a)
f.write(a)
f.close()

def review_class_log():
    try:
        with open("class_log.txt", "r") as file:

            log_contents = file.read()
            print("Class Log:")
            print(log_contents)

    except FileNotFoundError:
        print("No class log found for today.")

review_class_log()




# 17). You are developing a simple calculator program for a basic math tutoring app. One of the functionalities is division, where users can input two numbers to divide. You want to handle cases where the user accidentally or intentionally tries to divide by zero, and provide a friendly error message instead of crashing the program.

while True:
    try:
      x=int(input("enter x value :"))
      y=int(input("enter y value :"))

      result = x / y
      print("result :",result)
      break

    except ZeroDivisionError as z:
      print("Error: Cannot divide by zero.",z)

x=int(input("Enter the starting range : "))
y=int(input("Enter the endind range : "))
print("Armstrong numbers :")
for n in range(x,y):
    s=0
    a=str(n)
    for i in range(len(a)):
        s=s+int(a[i])**len(a) 
    if n==s:
        print(n)
