from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os

root = Tk()
root.title("Untitled - Notepad")
root.geometry('1080x1080')
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Uncomment this if you have a 'Notepad.png' icon
# icon = PhotoImage(file='Notepad.png')
# root.iconphoto(False, icon)

text_area = Text(root, font=("Times New Roman", 12))
text_area.grid(row=0, column=0, sticky=N+S+E+W)

scroller = Scrollbar(root, orient=VERTICAL, command=text_area.yview)
scroller.grid(row=0, column=1, sticky=N+S)

text_area.config(yscrollcommand=scroller.set)


def open_file():
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        with open(file, "r") as file_:
            text_area.insert(1.0, file_.read())


def open_new_file():
    root.title("Untitled - Notepad")
    text_area.delete(1.0, END)


def save_file():
    file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                filetypes=[("Text File", "*.txt*"), ("Word Document", '*.docx*'), ("PDF", "*.pdf*")])
    if file:
        with open(file, "w") as file_:
            file_.write(text_area.get(1.0, END))
        root.title(os.path.basename(file) + " - Notepad")


def exit_application():
    root.destroy()


def copy_text():
    text_area.event_generate("<<Copy>>")


def cut_text():
    text_area.event_generate("<<Cut>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def select_all():
    text_area.tag_add("sel", "1.0", "end")


def delete_last_char():
    text_area.delete("end-2c")


def about_notepad():
    mb.showinfo("About Notepad", "This is just another Notepad, but this is better than all others")


def about_commands():
    commands = """
Under the File Menu:
- 'New' clears the entire Text Area
- 'Open' clears text and opens another file
- 'Save As' saves your file in the same / another extension

Under the Edit Menu:
- 'Copy' copies the selected text to your clipboard
- 'Cut' cuts the selected text and removes it from the text area
- 'Paste' pastes the copied/cut text
- 'Select All' selects the entire text
- 'Delete' deletes the last character 
"""
    mb.showinfo(title="All commands", message=commands, width=60, height=40)


menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=open_new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command=exit_application)

menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=False)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
edit_menu.add_command(label='Delete', command=delete_last_char)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=False)
help_menu.add_command(label='About Notepad', command=about_notepad)
help_menu.add_command(label='About Commands', command=about_commands)

menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()
