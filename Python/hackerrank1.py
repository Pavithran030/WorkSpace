det=[]
n=int(input("Enter :"))
for i in range(0,n):
    na=input()
    sc=float(input())
    det.append([na,sc])
det.sort()
print(det)