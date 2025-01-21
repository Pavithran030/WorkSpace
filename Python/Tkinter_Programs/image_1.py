import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
window=tk. Tk()
count=0
def click():
    global count
    count+=1
    print(count)
image=tk.PhotoImage(file='sample.png')


#ttk.Label(window,text='Pavithran',font=('Algebrian,20,bold'),image=photo,compound='bottom').pack()
ttk.Button(window,text='Click',image=image,compound='bottom',command=lambda:click()).pack()
window.mainloop()