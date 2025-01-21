import tkinter as tk
from tkinter import ttk
car=tk.Tk()
car.geometry('400x200')
car.config(bg='sky blue')
#car.resizable(0,0)
def details():
    d=ent.get()
    print(d)

def delete():
    ent.delete(0,'end')

def space():
    ent.delete(len(ent.get())-1,'end')

ent=ttk.Entry(car,font=('poppins,10'))
ent.pack(side='left')

but_del=tk.Button(car,text='Delete',
    bg='green',
    fg='black',
    command=delete)
but_del.pack(ipadx=10,ipady=5,padx=10,side='right')

but_bac=tk.Button(car,text='Backspace',
    bg='green',
    fg='black',
    command=space)
but_bac.pack(ipadx=10,ipady=5,padx=5,side='right')

but=tk.Button(car,text='Submit',
    bg='green',
    fg='black',
    activebackground='green',
    activeforeground='black',
    command=details)
but.pack(ipadx=5,ipady=5,padx=20,pady=50)

car.mainloop()