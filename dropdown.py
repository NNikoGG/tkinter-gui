from tkinter import *
from PIL import ImageTk, Image
import emoji

root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

def show():
    my_label = Label(root, text=clicked.get())
    my_label.pack()
options = [
    "Arsenal",
    "Chelsea",
    "Manchester United",
    "Manchester City",
    "Tottenham Hotspurs"
]


clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()


b = Button(root, text="Show selection", command=show)
b.pack()


root.mainloop()