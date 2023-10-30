from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("window")

def open():
    global myImage
    top = Toplevel()
    top.title("New Window")
    myImage = ImageTk.PhotoImage(Image.open("images/goofy1.png"))
    myLabel = Label(top, image=myImage).pack()
    b2 = Button(top, text="Click to close new window", command=top.destroy).pack()

b = Button(root, text="Click to open new window", command=open).pack()

root.mainloop()