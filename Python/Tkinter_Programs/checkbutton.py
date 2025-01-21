import tkinter as tk
from tkinter import ttk
from tkinter import*
t=tk.Tk()
t.geometry('400x400')
tk.columngrid
mage=tk.PhotoImage(file='AIML.png')
ttk.Checkbutton(t,width=20,text='Check it',onvalue=1,offvalue=0,compound='center',image=mage).pack(padx=10,pady=40)
for i in range(3):
    ttk.Radiobutton(t,text="goog"
    ).pack()
t.mainloop()