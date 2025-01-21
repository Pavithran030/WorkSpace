print("Welcome to login ")
login={}
def ff2():
    fuser=input("Enter your old username : ")
    fpass=input("Enter a new password : ")
    if fuser in login[fuser]:
        login[fuser]=fpass
def nu():
    nuser=input("Enter new username : ")
    npas=input("Enter new password : ")
    if nuser in login:
        login[nuser]+=npas
    else:
        login[nuser]=npas
def log():
    user=input("Enter your username : ")
    pas=input("Enter your password : ")
    if (user in login):
        if pas in login[user]:
            print("You logined Successfully..!!")
        else:
            print("Incorrect password")
            ff2()
    else:
        print("Incorrect credential....")
        print("1.Forgot Username \n 2.Forgot Password")
        ch=int(input("Enter your choice : "))
        if ch==1:
            fuser=input("Enter your new username : ")
            fpass=input("Enter new password : ")
            login[nuser]=npas
        elif ch==2:
            ff2()
while True:
    print("1.New user \n2.Login \n3.Display Saved username and Password \n4.Exit")
    chose=int(input("Enter your choice : "))
    if chose==1:
        nu()
    elif chose == 2:
        log()
    elif chose==3:
        dis=input("Enter username to see your Password : ")
        if dis in login:
            print("Your Password is ",login[dis])
        else:
            print("The Username is not found..!!")
    else:
        break
print("Exit...")
