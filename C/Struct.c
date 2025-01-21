n=map(str,input().split())
tar=int(input())
for i,ind in enumerate(n):
  if tar==int(i):
    print(i,end="")
