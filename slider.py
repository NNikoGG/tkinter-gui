from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
horizontal = Scale(root, from_=0, to=1024, orient=HORIZONTAL)
vertical = Scale(root, from_=0, to=768)

horizontal.pack()
vertical.pack()

def slide():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


b = Button(root, text= "Change Window Size", command=slide).pack()

root.mainloop()