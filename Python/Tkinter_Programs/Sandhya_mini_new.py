import tkinter as tk
from math import *
from tkinter import *
import tkinter.ttk as ttk

men=Tk()
men.title("Project-1")
men.geometry('1520x1080')
men.configure(bg="white")
men.resizable(False,False)

sample=IntVar()
text1=IntVar()
text2=IntVar()
text3=IntVar()

def cle():
    text1.set("")
    text2.set("")
    text3.set("")
    sample.set("")

def area():
    a=float(text1.get())
    b=float(text2.get())
    option = men.combo.get()
    output = ""
    if option == "Square":
        output = a*a
    elif option == "Circle":
        output = 3.14*(a*a)
    elif option == "Rectangle":
        output = a*b
    elif option == "Triangle":
        output = (a*b)/2
        
    sample.set(output)

def perimeter():
    a=float(text1.get())
    b=float(text2.get())
    c=float(text3.get())
    option = men.combo.get()
    output = ""
    if option == "Square":
        output = 4*a
    elif option == "Circle":
        output = 2*(3.14)*a
    elif option == "Rectangle":
        output = 2*(a+b)
    elif option == "Triangle":
        output = a+b+c
        
    sample.set(output)
    
def root():
    a=float(text1.get())
    option = men.combo.get()
    output = ""
    if option == "Square Root":
        output = sqrt(a)
    sample.set(output)

def cube():
    a=float(text1.get())
    option = men.combo.get()
    output = ""
    if option == "Cube Root":
        output = a**(1. / 3) 
    sample.set(output)

def update_fields(event):
    option = men.combo.get()
    if option in ["Square", "Circle", "Square Root", "Cube Root"]:
        text1_entry.grid(row=1, column=1)
        text1_entry.place(x=10, y=350)
        text2_entry.grid_forget()
        text3_entry.grid_forget()
    elif option == "Rectangle":
        text1_entry.grid(row=1, column=1)
        text1_entry.place(x=10, y=350)
        text2_entry.grid(row=2, column=1)
        text2_entry.place(x=10, y=450)
        text3_entry.grid_forget()
    elif option == "Triangle":
        text1_entry.grid(row=1, column=1)
        text1_entry.place(x=10, y=350)
        text2_entry.grid(row=2, column=1)
        text2_entry.place(x=10, y=450)
        text3_entry.grid(row=3, column=1)
        text3_entry.place(x=10, y=550)
    else:
        text1_entry.grid_forget()
        text2_entry.grid_forget()
        text3_entry.grid_forget()

Label(men,text="Welcome To my site",font=('Arial',15,'bold'),bg='white').place(x=10,y=10)
Label(men,text="Calculate Area,perimeter of different Shapes and calculate the square root and cube root of the number",font=('Arial',15,'bold'),bg='white').place(x=10,y=50)
Label(men,text="Enter Input1",font=('Arial',15,'bold'),bg='white').place(x=20,y=300)
Label(men,text="Enter Input2",font=('Arial',15,'bold'),bg='white').place(x=20,y=400)
Label(men,text="Enter Input3",font=('Arial',15,'bold'),bg='white').place(x=20,y=500)
Label(men,text="Chooes Shapes and Roots ",font=('Arial',15,'bold'),bg='white').place(x=10,y=100)
Label(men,text="Calculate :",font=('Arial',15,'bold'),bg='white').place(x=200,y=600)
Label(men,text="Result :",font=('Arial',15,'bold'),bg='white').place(x=200,y=700)

text1_entry = Entry(men, width=20, textvariable=text1, font=('algerian',18), bg='white')
text2_entry = Entry(men, width=20, textvariable=text2, font=('algerian',18), bg='white')
text3_entry = Entry(men, width=20, textvariable=text3, font=('algerian',18), bg='white')

Button(men,text='Area',font=('Arial',10,'bold'),width=10,bg='pink',command=area).place(x=200,y=650)
Button(men,text='Permeter',font=('Arial',10,'bold'),width=10,bg='pink',command=perimeter).place(x=300,y=650)
Button(men,text='Root',font=('Arial',10,'bold'),width=10,bg='pink',command=root).place(x=400,y=650)
Button(men,text='Cube',font=('Arial',10,'bold'),width=10,bg='pink',command=cube).place(x=500,y=650)
Button(men,text='CLEAR',font=('Arial',10,'bold'),width=10,bg='pink',command=cle).place(x=600,y=650)

men.combo = ttk.Combobox(state="readonly", values=["Square", "Circle", "Rectangle", "Triangle","Square Root","Cube Root"])
men.combo.place(x=10, y=150)
men.combo.bind("<<ComboboxSelected>>", update_fields)

sample_label = Label(men, textvariable=sample, font=('Arial',20,'bold'), bg='white')
sample_label.place(x=350,y=700)

men.mainloop()