f=open('D:\\VS Codes\\Python\\Lab_Exercise\\result.txt','w')
o,a,b,c,d,u=0,0,0,0,0,0
per=0
sum=0
for i in range(1):
    
    lst=[]
    for j in range(7):
        k=input(f"Enter the name ,reg,5 sub grade,total,per {j+1}:")
        lst.append(k)
    for k in range(2,7):
        if k=='U':
            u+=10
        elif k=='A':
            a+=9
        elif k=='B':
            b+=8
        elif k=='C':
            c+=7
        elif k=='D':
            d+=6
        elif k=='U':
            u+=0
    sum=o+a+b+c+d+u
    print(sum)
    lst.append(sum)
    per=sum/5
    print(per)
    lst.append(per)
    lst=str(lst)
    f.write(lst)
    f.write("\n")
f.close