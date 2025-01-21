n=int(input())
dic={}
sum=0
for i in range(0,n):
    name,a,b,c=input().split()
    k=[a,b,c]
    dic[name]=k
query=input()
for i in dic[query]:
    sum+=int(i)
m=sum/3
print(format(m,".2f"))
    