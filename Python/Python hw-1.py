tup=((1,2,3,4),(5,6,8,9),(8,4,9,10),(56,88,48,55))
lst=[]
sum=0
for i in range(0,len(tup)):
    for j in range(0,len(tup[i])):
        sum+=tup[i][j]
    lst.append(sum/len(tup[i]))
print(lst)