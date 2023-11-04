from tkinter import *
import emoji

root = Tk()
root.title("Dropdown Menus")
root.geometry("400x400")

def show():
    selected = clicked.get()
    emoji_dict = {
        "Arsenal": "Bottle Team :face_with_tears_of_joy:",
        "Chelsea": "Finished Team :face_with_tears_of_joy:",
        "Manchester United": "Finished Team :face_with_tears_of_joy:",
        "Manchester City": "Oil Club :face_with_tears_of_joy:",
        "Tottenham Hotspurs": "No Trophy :face_with_tears_of_joy:"
    }
    emoji_text = emoji_dict.get(selected, "")
    my_label = Label(root, text=emoji.emojize(emoji_text))
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
