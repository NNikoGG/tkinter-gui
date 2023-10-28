from tkinter import *

root = Tk()
root.title("Frames")

myFrame = LabelFrame(root, text= "Test Frame", padx=10, pady=10)
myFrame.pack(padx=50, pady=50)

myLabel = Label(myFrame, text= "This is a frame!")
myLabel.pack()

myButton = Button(myFrame, text= "Exit Program", command=root.quit)
myButton.pack()


root.mainloop()