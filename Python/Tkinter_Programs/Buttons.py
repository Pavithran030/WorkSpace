import tkinter as tk 
from tkinter import ttk
def quit():
    print("Quitted Successfully....")

root=tk.Tk()
root.title('Buttons')
root.geometry('400x400')
tk.Button(root,text='CLICK',bg='green',fg='black',command=lambda:quit()).pack(padx=10,pady=10)
tk.Checkbutton(root,text='check',font=('poppins,20'),onvalue=True,offvalue=False).pack()
root.mainloop()