import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title('BLANK WINDOW')
#title=window.title()
root.geometry('600x400+90-90')#size of the window
message=tk.Label(root,text="NEW WINDOW FOR WORKSPACE........")
message.pack()


#to centrice the window screen

win_width=1200
win_height=800

#to get the dimension of the screen
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

#find the centre point
centerx=int(screen_width/2-win_width/2)
centery=int(screen_height/2-win_height/2)

#fix the position to the center point
root.geometry(f'{win_width}x{win_height}+{centerx}+{centery}')
root.resizable(False,False) # its does not allow to resize the windows  if give true we have able to resize it
root.title()

#display button on the windows
ttk.Button(root,text='Click',command=lambda:root.quit()).pack()



root.mainloop()#keep displaying the windows otherwise the windows doesnt show
