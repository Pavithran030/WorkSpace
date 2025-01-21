'''print("Welcome to login ")
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
    elif user not in login:
        print("Incorrect Username..")
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
print("Exit...")'''

import tkinter as tk

def ff2():
    fuser = entry_username.get()
    fpass = entry_password.get()
    if fuser in login:
        login[fuser] = fpass
        label_status.config(text="Password updated successfully.")
    else:
        label_status.config(text="Username not found.")

def nu():
    nuser = entry_username.get()
    npass = entry_password.get()
    if nuser in login:
        login[nuser] += npass
    else:
        login[nuser] = npass
        label_status.config(text="New user added successfully.")

def log():
    user = entry_username.get()
    pas = entry_password.get()
    if user in login:
        if pas == login[user]:
            label_status.config(text="Login Successful!")
        else:
            label_status.config(text="Incorrect password")
            ff2()
    else:
        label_status.config(text="Incorrect Username")

# Create the main window
root = tk.Tk()
root.geometry('300x300')
root.title("Login System")

# Create a dictionary to store login information
login = {}

# Labels
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)

label_status = tk.Label(root, text=" ")
label_status.grid(row=3, column=0, columnspan=2)

# Entry fields
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Buttons
button_login = tk.Button(root, text="Login", command=log)
button_login.grid(row=2, column=0)

button_new_user = tk.Button(root, text="New User", command=nu)
button_new_user.grid(row=2, column=1)

button_forgot_password = tk.Button(root, text="Forgot Password", command=ff2)
button_forgot_password.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()

