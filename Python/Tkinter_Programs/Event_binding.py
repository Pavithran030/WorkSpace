import tkinter as tk
from tkinter import ttk
def log(event):# handler 
    print(event)
car=tk.Tk()
car.geometry('600x600')
car.title('Temporary Screen')
ttk.Label(car,text='Workspace Window',font=('Algerian',20)).pack()
bt=ttk.Button(car,text='CLICK',command=lambda:car.quit())#pack(padx=10,pady=30)

bt.bind('<Return>')
#car.bind_class('Entry','<Control-V>')
 #Return refers to key to be used for action 
 # add used to add more than one handler for bing widget
bt.focus()
bt.pack(padx=200,pady=0,expand=True)
car.mainloop()