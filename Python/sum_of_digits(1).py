n=int(input("Enter a number :"))
sum=0
if n>0:
    while(n>0):
        k=n%10
        n=n//10
        sum+=k
    print(sum)
else :
    print("The given number is negative...")