import tkinter as tk
from tkinter import ttk
car=tk.Tk()
car.geometry('300x300')
car.resizable(0,0)
car.title('Login')
car.columnconfigure(0,weight=1)
car.columnconfigure(1,weight=3)
car.columnconfigure(2,weight=3)
#mail
k1=ttk.Label(car,text='Email')
k1.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)

ky=ttk.Entry(car)
ky.grid(column=1,row=0,sticky=tk.W,padx=5,pady=5)
#password
k2=ttk.Label(car,text='Password')
k2.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)

k3=ttk.Entry(car)
k3.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)

ty=ttk.Button(car,text="Sign in",command=lambda:car.quit())
ty.grid(column=2,row=2,sticky="nsew")


car.mainloop()