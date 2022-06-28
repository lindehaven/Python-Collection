'''tkinter-widget-example-2'''

import sys
if sys.version_info < (3,0,0):
    from Tkinter import Tk, Label, Entry, Button, INSERT
    from Tkinter import tkMessageBox as mbox
else:
    from tkinter import Tk, Label, Entry, Button, INSERT
    from tkinter import messagebox as mbox

def show_name():
    mbox.showinfo('Name', 'You have written: '+name.get())

root = Tk()
root.geometry('400x150')
Label(root, text='Enter name: ',
      font = ('Arial', 14, 'normal'), fg='yellow',
      bg= 'blue').grid(row=0, column=0)
name=Entry(root, width=40)
name.grid(row=0, column=1, columnspan=5)
b = Button(root, text='Show name', command=show_name)
b.grid(row=1, column=3)
name.insert(INSERT, '')
root.mainloop()
