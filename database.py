from tkinter import *
from PIL import ImageTk, Image
import emoji
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x400")

# Creating a database
conn = sqlite3.connect("address_book.db")

# Creating a cursor
c = conn.cursor()

# Creating a table
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")


# Commit changes

conn.commit()

# Close connection
conn.close()

root.mainloop()