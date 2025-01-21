import tkinter as tk 
from tkinter import ttk 
def submit():
    print("Submitted successfully..")

def delete():
    en.delete(0,'end')
def back():
    en.delete(len(en.get())-1,'end')
root=tk.Tk()
ttk.Label(root,text='Note pad',font=('ALGERIAN,30')).pack()
en=tk.Entry(root,font=('poppins,20'),fg='dark green',bg='light blue')
en.pack(side='left')
but=ttk.Button(root,text='Submit',command=submit)
but.pack(side='right')

delt=ttk.Button(root,text='Delete',command=delete)
delt.pack(padx=5,pady=5,side='right')

back=ttk.Button(root,text='Backspace',command=back)
back.pack(side='right')

root.mainloop()

