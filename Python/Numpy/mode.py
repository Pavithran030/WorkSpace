# import hackerrank
# a,b=map(int,(input().split()))
# # b=int(input())
# a,b,c,d,e=hackerrank.pro(a,b)
# print(f"Addition is {a}\nSubtraction is {b}\nMultiplication is {c}\nDivision is {d}\nFloor Division is {e}")
n=int(1010)
n1=""
while n!=0:
    n1=str(n%2)+n1
    n=n//10

print(int(n1),end="")
