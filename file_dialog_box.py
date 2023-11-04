from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Dialog Box")

my_img_label = Label(root)
my_img_label.pack()

def open():
    global my_img
    global my_img_label
    if my_img_label.winfo_exists():
        my_img_label.destroy()
    root.filename = filedialog.askopenfilename(initialdir="./images/", title="Select a file", filetypes=(("PNG files", "*.png"),("All files", "*.*")))
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(root, image=my_img)
    my_img_label.pack()

b = Button(root, text= "Click to open file", command=open)
b.pack()

root.mainloop()
