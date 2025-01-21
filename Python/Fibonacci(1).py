n=int(input("Enter the number "))
t1=0
t2=1
print(t1,t2,end=" ")
for i in range(0,n):
    k=int(t1+t2)
    print(k,end=" ")
    t1=t2
    t2=k
