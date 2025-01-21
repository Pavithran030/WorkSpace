import tkinter as tk
from tkinter import PhotoImage

car = tk.Tk()
st = tk.Frame(car).pack(padx=10, pady=10, fill='x', expand=True)
car.geometry('400x400')

photo = PhotoImage(file='AIML.png')
car.title('Temporary Screen')
t1 = tk.Label(car, text='HAI', font=('Algerian', 10, 'bold'), bg='pink', fg='green', bd=20, relief='flat', image=photo)
t2 = tk.Label(car, text='KANIJA', font=('Copperplate Gothic Bold', 10), bg='light blue', fg='red')
t3 = tk.Label(car, text='HOW ARE YOU', font=('Copperplate Gothic Bold', 10), bg='gray', fg='yellow')

t1.pack(side=tk.TOP, padx=10, fill='none', anchor='center')
t2.pack(side=tk.LEFT, padx=20, fill='none', anchor='center', expand=True)
t3.pack(side=tk.TOP, fill='none', anchor='s')
car.mainloop()