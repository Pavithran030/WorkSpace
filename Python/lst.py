
lst=[0,1,2,3,4,5]
last1=[]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)-1):
        if lst[i]==lst[j]:
            lst[j]="*" 
    if lst[i]!="*":
        last1.append(lst[i]) 
print(last1)

print(__name__)