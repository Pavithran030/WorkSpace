import random
tu=['O','A','B','C','D','U']
f=open('D:\\VS Codes\\Python\\Lab _Exercise\\result.txt','w')
n=int(input("Enter the number of students : "))
for i in range(n):
    sum=0
    per=0
    lst=[]
    a=input(f"Enter the name of student{i+1}: ")
    b=int(input(f"Enter student {i+1} Reg no: "))
    lst.append(a)
    lst.append(b)
    for j in range(5):
        k=random.choice(tu)
        lst.append(k)
    for k in range(2,7):
        match lst[k]:
            case 'O':
                sum+=10
            case 'A':
                sum+=9
            case 'B':
                sum+=8
            case 'C':
                sum+=7
            case 'D':
                sum+=6
            case 'U':
                sum+=0
    lst.append(sum)
    per=(sum/5)*10
    lst.append(per)
    lst=str(lst)
    f.write(lst)
    f.write("\n")
    print(f"Total number of sytudents details added :{i+1}")
print("Details Successfully Added👍👍👍👍👍👍👍👍")
f.close

# TO VIEW DETAILS STORED IN THE FILE............

f=open('D:\\VS Codes\\Python\\Lab _Exercise\\result.txt','r')
k=f.read()
print(k)

# ANALYSIS A FILE BASED ON A CONDITION
f=open('D:\\VS Codes\\Python\\Lab _Exercise\\result.txt','r')
i=f.readlines()
for j in i:
    lst=eval(j)
    if lst[8]>=90:
        print("Students who score 90% and above")
        print(lst[0])
    elif lst[8]>=80 and lst[8]<90:
        print("Students who score equal to or above 80% and below 90%")
        print(lst[0])
    elif lst[8]>=70 and lst[8]<80:
        print("Students who score equal to or above 70% and below 80%")
        print(lst[0])
    elif lst[8]<70:    
        print("Students who score below 70%")    
        print(lst[0])
    for i in range(2,8):
        if lst[i]=='U':
            print("Students who got Arrear...")    
            print(lst[0])
            break