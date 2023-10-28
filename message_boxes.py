from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def buttonClick(input):
    if input == 1:
        response = messagebox.showinfo("Info", "Your PC is about to blow up because of this code")
        Label(root, text=response).pack()
    if input == 2:
        response = messagebox.showwarning("Warning", "Your PC is about to blow up because of this code!")
        Label(root, text=response).pack()
    if input == 3:
        response = messagebox.showerror("Error", "Your PC is about to blow up because of this code!")
        Label(root, text=response).pack()
    if input == 4:
        response = messagebox.askquestion("Question", "Your PC is about to blow up because of this code?")
        Label(root, text=response).pack()
    if input == 5:
        response = messagebox.askokcancel("Ok/Cancel", "Your PC is about to blow up because of this code")
        Label(root, text=response).pack()
    if input == 6:
        response = messagebox.askyesno("Ask Yes/No", "Your PC is about to blow up because of this code. You good with that?")
        Label(root, text=response).pack()


showinfo_button = Button(root, text= "Show Info", command=lambda:buttonClick(1))
showwarning_button = Button(root, text= "Show Warning", command=lambda:buttonClick(2))
showerror_button = Button(root, text= "Show Error", command=lambda:buttonClick(3))
askquestion_button = Button(root, text= "Ask Question", command=lambda:buttonClick(4))
askokcancel_button = Button(root, text= "Ask Ok/Cancel", command=lambda:buttonClick(5))
askyesno_button = Button(root, text= "Ask Yes/No", command=lambda:buttonClick(6))

showinfo_button.pack()
showwarning_button.pack()
showerror_button.pack()
askquestion_button.pack()
askokcancel_button.pack()
askyesno_button.pack()

root.mainloop()