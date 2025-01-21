from customtkinter import*
root=CTk()
def button_event():
    print('button pressed')

button =CTkButton(root, text='CTkButton', width=140, height=28)
button.place(x=10, y=10)
entry = CTkEntry(root, placeholder_text='CTkEntry', width=140, height=28)
entry.place(x=10, y=10)
root.mainloop()