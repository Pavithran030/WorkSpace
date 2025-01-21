import tkinter as tk
from tkinter import ttk
car=tk.Tk()
car.geometry('600x600')
car.resizable(0,0)
car.title('Temporary Screen')
ttk.Label(car,text='Details',font=('Algerian',20)).pack()
ttk.Label(car,text='Name   :',font=('Poppins',20)).place(relx=0.16,rely=0.1,anchor='w')
ttk.Label(car,text='Age    :',font=('Poppins',20)).place(relx=0.16,rely=0.2,anchor='w')
ttk.Label(car,text='Gender :',font=('Poppins',20)).place(relx=0.16,rely=0.3,anchor='w')

ttk.Entry(car,text='CLICK').pack(ipadx=30,ipady=10,padx=40,pady=10,anchor='center')
ttk.Entry(car,text='CLICK').pack(ipadx=30,ipady=10,padx=40,pady=10,anchor='center')
ttk.Entry(car,text='CLICK').pack(ipadx=30,ipady=10,padx=40,pady=10,anchor='center')
py=tk.Label(car,text='CLICK',bg='blue',fg='red').place(relx=0.5,rely=0.4,width=90,height=20,anchor='center')
car.mainloop()