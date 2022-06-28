'''tkinter-widget-example-1'''

import sys
if sys.version_info < (3,0,0):
    from Tkinter import Tk, Label, Button
    from Tkinter import tkMessageBox as mbox
else:
    from tkinter import Tk, Label, Button
    from tkinter import messagebox as mbox

def hello():
    mbox.showinfo('Hello', 'Hi there!')

root = Tk()
root.geometry('160x120')
text = Label(root, text='Hello, world!')
text.pack()
b1 = Button(root, text='Say hi!', command=hello)     # Skapa en knapp som anropar hello
b1.pack()                                            # som är en callback-funktion
b2 = Button(root, text='Exit', command=root.destroy) # Skapa en knapp som tar bort
b2.pack()                                            # objektet root vilket avslutar.
root.mainloop()
