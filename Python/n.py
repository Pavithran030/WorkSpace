n=map(str,input().split())
tar=input()
c=0
if tar not in n:
    print("-1")
else:
    for i in n:
        c+=1
        if int(tar)==int(i):
            print(c-1,end="")