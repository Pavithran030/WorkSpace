import tkinter as tk
from tkinter import ttk
car=tk.Tk()
#st=ttk.Frame(car).pack(padx=10,pady=10,fill='x',expand=True)
car.geometry('600x600')
car.title('Temporary Screen')
ttk.Label(master=car,text='Workspace Window',bg='blue',fg='green').pack(side=tk.BOTTOM)
car.mainloop()
