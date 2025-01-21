num=int(input("Enter a number : "))
g=0
while num > 0:
    k=num%10
    num=num//10
    g+=k
print("The sum is : ",g)