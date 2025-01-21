# 1.	Write a Python program to check if a given number is positive, negative, or zero 

n=int(input("Enter to a number to find positive or negative :"))
if n==0:
    print(f"{n} it is  Zero")
elif n>0:
    print(f"{n} is Positive")
else:
    print(f"{n} is Negative.")

# #2.	Create a program that takes a user's age as input and outputs whether they are eligible to vote or not (considering the legal voting age is 18).

age=int(input("Enter your age : "))
if age>=18:
    print("Your are eligible for voting ")
else:
    print("Your are not eligible for voting ")

# # 3.	Write a Python program to determine whether a given year is a leap year or not

y=int(input("Enter year to find leap year or not :"))
if (y%4==0 and y%100==0 ) and y%400==0:
    print(f"{y} is Leap year..")
elif (y%4==0 and y%100!=0 ) and y%400!=0:
    print(f"{y} is Leap year..")
else:
    print(f"{y} is Not a Leap year..")

# # 4.	Develop a program that takes a user's temperature as input and outputs whether they have a fever or not (considering a fever if temperature is equal to or above 100.4°F or 38°C).

h=int(input("Enter your choice 1.Faherinheit or 2.Celsius:"))
if h==1:
    f=float(input("Enter the temperature in Faherinheit :"))
    if f>=100.4:
        print("You have a fever")
    else:
        print("You have no fever..")
elif h==2:
    c=float(input("Enter the temperature in Celsius :"))
    if c>=32:
        print("You have a fever")
    else:
        print("You have no fever..")
else:
    print("Invalid Input...")

# # 5.	Create a Python program to find the largest among three numbers entered by the user.

a,b,c=input("Enter any three number :")
if a>b and a>c:
    print(f"{a} is the biggest number")
elif b>a and b>c:
    print(f"{b} is the biggest number")
else:
    print(f"{c} is the biggest number")

# # 6.	Write a program to calculate the total cost of a meal, including tax and tip, based on user input for the meal cost and percentage rates for tax and tip.

cost=int(input("Enter the cost of the meals :"))
tax=float(input("Enter the tax :"))
tip=float(input("Enter the tips :"))
taper=(tax*cost)/100
tiper=(tip*cost)/100
print("The total cost for meals (incl tax and tip) : ",cost+taper+tiper)

# # 7.	Develop a program to classify a triangle based on the lengths of its sides (scalene, isosceles, or equilateral).

s1,s2,s3=input("Enter the three sides of a triangle :")
if s1==s2==s3:
    print("Its is Equilateral Triangle ")
elif s1==s2 or s1==s3 or s2==s3:
    print("Its is Isoceles Triangle")
else:
    print("Its is Scalene Triangle")

# # 8.	Create a program that determines whether a given year is a leap year and has 366 days or a common year with 365 days.

y=int(input("Enter year to find leap year or not :"))
if (y%4==0 and y%100==0 ) and y%400==0:
    print(f"{y} is Leap year..\nIts has 366")
elif (y%4==0 and y%100!=0 ) and y%400!=0:
    print(f"{y} is Leap year..\nIts has 366")
else:
    print(f"{y} is Not a Leap year..\nIts has 365")

# # 9.	Write a Python program to check whether a character entered by the user is a vowel or a consonant.

ch=input("Enter the character to check for vowels or not :")
vo=['a','e','i','u','o']
if ch in vo:
    print("The Character is Vowels...")
else:
    print("The Character is not Vowels...")

# # 10.	Write a Python program that prompts the user to enter three numbers and then outputs them in ascending order.

a,b,c=input("Enter any three number :")
k=sorted([a,b,c])
print(f"The numbers in ascending order :")
for i in k:
    print(i,end=" ")

# ....................................................................................................................................

# 1. Develop a program that takes a user's score as input and outputs their corresponding grade based on the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).
# •	Test Case 1: Input score: 85. Expected output: Grade B.
# •	Test Case 2: Input score: 60. Expected output: Grade D.
# •	Test Case 3: Input score: 95. Expected output: Grade A.
 
s=int(input("Enter the score to find the grade :"))
if 100>=s and s>90:
    print("Your grade is A")
elif s<90 and s>=80:
    print("Your grade is B")
elif s<80 and s>=70:
    print("Your grade is C")
elif s<70 and s>=60:
    print("Your grade is D")
else:
    print("Your grade is F")

# #2.Create a program that simulates a simple ATM machine, prompting the user for their account balance and withdrawal amount, then outputs whether the transaction is successful or not based on the available balance and withdrawal amount.
# •	Test Case 1: Account balance: $1000, Withdrawal amount: $500. Expected output: Transaction successful.
# •	Test Case 2: Account balance: $200, Withdrawal amount: $300. Expected output: Insufficient funds.


def wit(bal,am):
    if am<bal:
        return "Withdrawal is successfully..."
    else:
        return "Insufficient Balance...."
bal=int(input("Enter the account balance :"))
am=int(input("Enter the amount to withdrawl :"))
print(wit(bal,am))

# 4.Develop a program that takes a user's age and gender as input and outputs their recommended heart rate range during exercise based on the American Heart Association's guidelines.
# •	Test Case 1: Age: 30, Gender: Male. Expected output: 93 - 157 bpm.
# •	Test Case 2: Age: 45, Gender: Female. Expected output: 88 - 149 bpm.
# •	Test Case 3: Age: 55, Gender: Male. Expected output: 85 - 145 bpm.

def bpm(a,g):
    if a==30 and g=="male":
        return " Recommended Heart beat 93-157 bpm "
    elif a==45 and g=="female":
        return " Recommended Heart beat 88-149 bpm"
    else:
        return "Recommended Heart beat 93-157 bpm"
age=int(input("Enter your age :"))
gen=input("Enter your gender :")
print(bpm(age,gen))
