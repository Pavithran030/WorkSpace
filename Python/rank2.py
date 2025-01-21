N = int(input())
lst=[]
for i in range(N):
    ty=input()
    if ty in "insert":
        i=int(input())
        v=int(input())
        lst.insert(i,v)
    elif ty in "remove":
        k=int(input())
        lst.remove(k)
    elif ty in "append":
        s=int(input())
        lst.append(s)
    elif ty in "sort":
        lst.sort()
    elif ty in "pop":
        lst.pop()
    elif ty in "reverse":
        lst.reverse()
    elif ty in "print":
        print(lst)