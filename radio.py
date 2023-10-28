from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

myLabel = Label(root, text="Pick your favorite team!")
myLabel.pack()


# Putting the team names in a tuple inside a list as a text and unique identifier pair for the radio buttons
TEAMNAMES = [
    ("Arsenal", "Arsenal"),
    ("Manchester United", "Manchester United"),
    ("Chelsea", "Chelsea"),
    ("Liverpool", "Liverpool"),
    ("Tottenham Hotspur", "Tottenham Hotspur")
]

# IntVar for integer variable
# StringVar for string variable
team = StringVar()
team.set("Arsenal")

# Running a loop to pack all the 4 buttons for fewer lines of code
for text, teamname in TEAMNAMES:
    Radiobutton(root, text= text, variable=team, value=teamname, command=lambda: buttonClick(team.get())).pack(anchor=W)

# Function to display the name of the team
# It receives the parameter from the radio button clicks
def buttonClick(value):
    myLabel = Label(root, text= value)
    myLabel.pack()

# Displays the team name as soon as you click submit
myButton = Button(root, text="Submit", command=lambda: buttonClick(team.get()))
myButton.pack()

root.mainloop()