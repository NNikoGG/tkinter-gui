from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")

def show():
    my_label = Label(root, text=var.get()) 
    my_label.pack()

var = StringVar()

c = Checkbutton(root, text= "Click here to Select/Deselect", variable=var, onvalue="Selected", offvalue="Deselected")
c.deselect()
c.pack()

b = Button(root, text="Show Status", command=show).pack()


root.mainloop()