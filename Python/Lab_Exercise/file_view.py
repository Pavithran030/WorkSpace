# TO VIEW DETAILS STORED IN THE FILE............

# f=open('D:\\VS Codes\\Python\\Lab _Exercise\\result.txt','r')
# k=f.read()
# print(k)

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