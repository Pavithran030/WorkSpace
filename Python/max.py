#Find max and min of a number without using relational  operator

a,b,c=input("Enter any three number:")
print(max(a,b,c))
print(min(a,b,c))

#Write a Python program to find if a given number is odd or even without using % operator.

a=int(input("Enter a number : "))
if a&1 ==0:
    print(a,"is Even Number")
else:
    print(a,"is odd Number")

#Write a Python program to find whether a given number is divisible by 7 or not without using % operator
    
a=int(input("Enter a number : "))
divisor=7
while a>=divisor: #ex:a=10 10>=7(t),so a=10-7=3;next a=3 3>=7 (f) loop end 
    a-=divisor
if a==0:
    print("The number is divisible by 7")
else:
    print("Its is not divisible by 7")

#Write a Python program to implement Tuple operations.

tup=('1','2','3','4','5','6')
print(tup)

print(tup[4])

print(tup[3:6])

print(len(tup))

tup1=('7','8','9','10')

print(tup+tup1)


