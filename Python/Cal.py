import math
print("Calculator")
while(1):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modules\n6.Float division\n7.Square root\n8.Power\n9.Factorial\n10.Exiting\n")
    n=int(input("\nEnter the operation u want to Form "))
    if n==1:
        print("Addition\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Addition of two number is : ",num1 + num2)
    elif n==2:
        print("Subtraction\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Subtraction of two number is : ",num1 - num2)
    elif n==3:
        print("Multiplication\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Multiplication of two number is : ",num1 * num2)
    elif n==4:
        print("Division\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Division of two number is : ",num1/num2)
    elif n==5:
        print("Modules\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Modules of two number is : ",num1 % num2)
    elif n==6:
        print("Float Division\n")
        num1=int(input("Enter the number1: "))
        num2=int(input("Enter the number2: "))
        print("Float division of two number is : ",num1//num2)
    elif n==7:
        print("Square Root\n")
        number=int(input("Enter the number: "))
        print("Square Root of the  number is : ",math.sqrt(number))
    elif n==8:
        print("Power\n")
        number=int(input("Enter the number: "))
        power=int(input("Enter the power: "))
        print("power of the number is : ",pow(number,power))
    elif n==9:
        print("Factorial\n")
        number=int(input("Enter number:"))
        fact=1
        while(number>0):
            fact=fact*number
            number=number-1
        print("Factorial of the number is: ")
        print(fact)
        break
    elif n==10:
        print("Exiting....")
    else:
        print("invalid opertaion")