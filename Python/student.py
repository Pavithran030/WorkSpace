stu=[]
stu1=[]
sum=0
def add():
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    grade=input("Enter Grade : ")
    stu1=[name,age,grade]
    stu.append(stu1)
def upda():
    per=input("Enter the name of the student to update the details :")
    if per in stu:
        k=index(per)
    for i in range(k,k+1):
        for i in range(0,len(stu[k])):
            std[2]=input("Enter new grade :")
        
def gra():
    for i in range(0,len(stu)):
        sum=sum+stu[i][2]
    print("the total grade of all student is :"(sum/len(stu)))
    
def view():
    na=input("Enter the name to dispaly the details : ")
    for j in na:
        print("Name :",stu[j][0])
        print("Age :",stu[j][1])
        print("Grade :",stu[j][2])
print("1.Add New Details \n2.Update Grade \n3.Grade Average \n4.View Details \n5.Exit")

while True:
    choice=int(input("Enter Your choice :"))
    if choice==1:
        add()
        stu.append(stu1)
    elif choice==2:
        upda()
    elif choice==3:
        gra()
    elif choice==4:
        view()
    else:
        if choice==5:
            break
print("Exit...!!!!")