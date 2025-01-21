cart=[]
def menu():
    print("1.Add item \n2.Remove item \n3.View item \n4.Total price \n5.Exit")
    c=int(input("Enter your choice :"))
    if c==1:
        a()
    elif c==2:
        r()
    elif c==3:
        v()
    elif c==4:
        t()
    else:
        print("Exit...!!")
def a():
    pro=input("Enter the name of the product : ")
    pri=input("Enter the product price : ")
    qua=int(input("Enter the quantity : "))
    tup=(pro,pri,qua)
    cart.append(tup)
    print("Added Successfully...!!")
    menu()
def r():
    ra=input("Enter the product name to remove : ")
    for i in cart:
        cart.remove(i)
    menu()
def v():
    na=input("Enter the product name : ")
    for i in range(0,len(cart)):
        print(index(i))
        print(i)
    menu()
def t():
    sum=0
    for i in range(0,len(cart)):
        sum+=int(cart[i][1])
    print("The total price for the item in your cart =Rs.",sum)
    menu()
menu()