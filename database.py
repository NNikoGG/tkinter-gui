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
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
'''

def submit():
	# Creating a database
	conn = sqlite3.connect("address_book.db")

	# Creating a cursor
	c = conn.cursor()

	# Inserting the values into the table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
		   {
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
		   		'zipcode': zipcode.get()
		   	})
	
	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()
	
    # Clear the text boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)


def show():
	# Creating a database
	conn = sqlite3.connect("address_book.db")

	# Creating a cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# Show results in GUI
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(column=0, row=8, columnspan=2,)

	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()

# Creating textboxes
f_name = Entry(root, width=30)
f_name.grid(column=1, row=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(column=1, row=1)

address = Entry(root, width=30)
address.grid(column=1, row=2)

city = Entry(root, width=30)
city.grid(column=1, row=3)

state = Entry(root, width=30)
state.grid(column=1, row=4)

zipcode = Entry(root, width=30)
zipcode.grid(column=1, row=5)

# Creating textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(column=0, row=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(column=0, row=1)

address_label = Label(root, text="Address")
address_label.grid(column=0, row=2)

city_label = Label(root, text="City")
city_label.grid(column=0, row=3)

state_label = Label(root, text="State")
state_label.grid(column=0, row=4)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(column=0, row=5)

# Submit button

submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(column=0, row= 6, padx=10, pady=10, columnspan=2, ipadx=100)


# Show button
show_btn = Button(root, text= "Show query", command=show)
show_btn.grid(column=0,row=7, padx=10, pady=10, columnspan=2, ipadx=137)

# Commit changes

conn.commit()

# Close connection
conn.close()

root.mainloop()