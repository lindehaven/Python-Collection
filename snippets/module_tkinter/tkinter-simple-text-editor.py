'''tkinter-simple-text-editor

Simple Text Editor in Python (STEP) using Tkinter/tkinter.
There are a few things to do before this actually can be used as a text editor.
Check out the TODO comments in the code and fix them.
'''

# TODO: Clean up pylint issues
# TODO: Only import what is used
import sys
if sys.version_info < (3,0,0):
    import Tkinter
    from Tkinter import *
    import tkMessageBox as mbox
    import tkFileDialog as fdialog
else:
    import tkinter
    from tkinter import *
    from tkinter import messagebox as mbox
    from tkinter import filedialog as fdialog


class SimpleEditor(Frame):
    '''Simple Editor class'''

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.version = "0.0.1"
        self.program = "STEP"
        self.file_name = ""
        self.init_user_interface()

    def init_user_interface(self):
        '''Initializes the user interface'''
        self.set_title()
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open...", command=self.on_open)
        # TODO: "Save"
        # TODO: "Save As..."
        # TODO: "Close"
        fileMenu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=fileMenu)
        helpMenu = Menu(menubar)
        helpMenu.add_command(label="About " + self.get_program(),
                             command=self.about)
        menubar.add_cascade(label="Help", menu=helpMenu)

        self.scr = Scrollbar(self)
        self.txt = Text(self)
        self.scr.pack(side=RIGHT, fill=Y)
        self.txt.pack(fill=BOTH, expand=1)
        self.scr.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scr.set)
        self.txt.insert(END, "")
        self.txt.pack(fill=BOTH, expand=1)

    def set_title(self):
        '''Sets the window title'''
        if not self.get_file_name():
            self.set_file_name("untitled.txt")
        self.parent.title(self.get_file_name() + " - " + self.get_program())

    def on_open(self):
        '''Opens file'''
        # TODO: Check if an open file has been changed before opening another
        filetypes = [("Python files","*.py"),("All files","*")]
        fn = fdialog.askopenfilename(title = "Choose file to open",
                                     filetypes = filetypes)
        if fn != '':
            self.set_file_name(fn)
            self.set_title()
            self.txt.delete(1.0, END)
            with open(self.get_file_name(), "r") as f:
                self.txt.insert(END, f.read())

    # TODO: "Save"

    # TODO: "Save As..."

    # TODO: "Close"

    def on_exit(self):
        '''Exits application'''
        # TODO: Check if a file is open and if it has been changed before exit
        self.quit()

    def about(self):
        '''Shows information about application'''
        mbox.showinfo("About " + self.get_program(), self.get_program_version())

    def get_program(self):
        '''Gets application name'''
        return self.program

    def get_program_version(self):
        '''Gets application name and version'''
        return self.program + " " + self.version

    def get_file_name(self):
        '''Gets file name'''
        return self.file_name

    def set_file_name(self, file_name):
        '''Sets application name'''
        self.file_name = file_name


def main():
    '''Creates a GUI for the application'''
    root = Tk()
    root.geometry("600x400")
    app = SimpleEditor(root)
    root.mainloop()

if __name__ == '__main__':
    main()
