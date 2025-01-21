check=""
ll1=""
pp1=""
l1=[]
p1=[]
def log():
    print("Welcome to login page")
def account():
    lo=input("Account name ")
    pa=input("Login password ")
    if lo in l1:
        if pa in p1:
            print("You login in sucessfully ")
    else:
        print("Your account is not exists")
    if "pa"!="p1":
        print("Incorrect Password")
        repas=input("Click type Yes to change the password")
        if repas=="yes":
            p1=input("Enter new password for your account :")
            pa.clear()
            p1=pa
            print("Password changed successfully")
            log()
            account()
        else:
            print("Unable to login sorry..!!!")
    else:
        print("Create a new account..................................")
        #account()
def new_account():
    ll1=input("Create new Account :")
    pp1=input("Password :")
    l1.append(ll1)
    p1.append(pp1)
log()
print("New user(Yes) or Old user (No)")
check=input("Yes or No : ")
if check=="yes":
    new_account()
else:
    account()
log()
account()
