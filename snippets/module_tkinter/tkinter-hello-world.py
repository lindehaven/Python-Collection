import sys
if sys.version_info < (3,0,0):            # Kolla om Python version är lägre än 3.0.0.
    from Tkinter import Tk, Label         # Använd Tkinter för version 2. Importera
                                          # endast det som används.
else:
    from tkinter import Tk, Label         # Använd tkinter för version 3. Importera
                                          # endast det som används.

root = Tk()                               # Skapa ett fönster med titelrad och knappar.
text = Label(root, text="Hello, world!")  # Skapa en text-widget som hör till fönstret.
text.pack()                               # Packa in text-widget och gör den synlig.
root.mainloop()                           # Starta tkinter som avlyssnar användarens
                                          # aktioner och ritar om fönstret.
