from tkinter import *
from PIL import ImageTk, Image

root = Tk()

myLabel = Label(root, text="Pick your favorite team!")
myLabel.pack()

TEAMNAMES = [
    ("Arsenal", "Arsenal"),
    ("Manchester United", "Manchester United"),
    ("Chelsea", "Chelsea"),
    ("Liverpool", "Liverpool"),
    ("Tottenham Hotspur", "Tottenham Hotspur")
]

team = StringVar()
team.set("Arsenal")

for text, teamname in TEAMNAMES:
    Radiobutton(root, text= text, variable=team, value=teamname, command=lambda: buttonClick(team.get())).pack(anchor=W)

def buttonClick(value):
    myLabel = Label(root, text= value)
    myLabel.pack()

# Radiobutton(root, text= "Option 1", variable=r, value=1, command=lambda: buttonClick(r.get())).pack()
# Radiobutton(root, text= "Option 2", variable=r, value=2, command=lambda: buttonClick(r.get())).pack()

# myLabel = Label(root, text= r.get())
# myLabel.pack()

myButton = Button(root, text="Submit", command=lambda: buttonClick(team.get()))
myButton.pack()

root.mainloop()