#Import the required Libraries
from  tkinter import *
from tkinter import filedialog

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x450")

#Function Upload File
def upload_file():
    global txt
    f_types = [('Text Files', '*.txt')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    # Program to read the entire file using read() function
    file = open(filename, "r")
    content = file.read()
    print(content)
    TextBox.insert(END, content)
    TextBox.insert(END, "\n")
    file.close()


TextBox = Text(win, height=10, width=45)
TextBox.pack(pady=20)

#Create a Button to validate Entry Widget
Button(win, text= "Upload File",width= 20, command= upload_file).pack(pady=20)

win.mainloop()