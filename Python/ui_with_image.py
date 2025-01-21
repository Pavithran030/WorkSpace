import tkinter as tk
from tkinter import ttk
car=tk.Tk()
car.geometry('200x200')
#car=title('AIML')
photo=PhotoImage(file='D:\\Downloads')
ttk.Button(car,image=photo).pack()

car.mainloop()
