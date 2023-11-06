from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import emoji
import sqlite3

root = Tk()
root.title("Database")
root.geometry("350x450")

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
        
def save():
	# Creating a database
	conn = sqlite3.connect("address_book.db")

	# Creating a cursor
	c = conn.cursor()

	# Query the database
	c.execute("""UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode       
		
		WHERE oid = :oid""",
		{
			'first': f_name_editor.get(),
			'last': l_name_editor.get(),
			'address': address_editor.get(),
			'city': city_editor.get(),
			'state': state_editor.get(),
			'zipcode': zipcode_editor.get(),
			'oid': delete_entry.get()
		})
	
	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()

	# Close the window
	editor.destroy()

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

	# Display results in GUI
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(column=0, row=12, columnspan=2,)

	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()

def delete():
	# Creating a database
	conn = sqlite3.connect("address_book.db")

	# Creating a cursor
	c = conn.cursor()

	# Query the database
	c.execute("DELETE FROM addresses WHERE oid = " + delete_entry.get())
	
	# Commit changes
	conn.commit()
	
	# Close connection
	conn.close()

def edit():
	global editor
	editor = Tk()
	editor.title("Edit a record")
	editor.geometry("387x200")

	val = delete_entry.get()

	if not val.isdigit():
		response = messagebox.showerror("Error", "Please enter a valid primary key")
		error_msg = Label(root, text=response)
		error_msg.grid(column=0, row=0)

	# Creating global variables for updating records
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor

	# Creating a database
	conn = sqlite3.connect("address_book.db")

	# Creating a cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT * FROM addresses WHERE oid = " + delete_entry.get())
	records = c.fetchall()
	
	# Creating textboxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(column=1, row=0, padx=20, pady=(10,0))

	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(column=1, row=1)

	address_editor = Entry(editor, width=30)
	address_editor.grid(column=1, row=2)

	city_editor = Entry(editor, width=30)
	city_editor.grid(column=1, row=3)

	state_editor = Entry(editor, width=30)
	state_editor.grid(column=1, row=4)

	zipcode_editor = Entry(editor, width=30)
	zipcode_editor.grid(column=1, row=5)

	# Creating textbox labels
	f_name_label = Label(editor, text="First Name")
	f_name_label.grid(column=0, row=0, pady=(10,0))

	l_name_label = Label(editor, text="Last Name")
	l_name_label.grid(column=0, row=1)

	address_label = Label(editor, text="Address")
	address_label.grid(column=0, row=2)

	city_label = Label(editor, text="City")
	city_label.grid(column=0, row=3)

	state_label = Label(editor, text="State")
	state_label.grid(column=0, row=4)

	zipcode_label = Label(editor, text="Zipcode")
	zipcode_label.grid(column=0, row=5)

	# Display existing record
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])	

	# Create a save button
	save_btn = Button(editor, text= "Save changes", command=save)
	save_btn.grid(column=0, row=6, padx=10, pady=10, columnspan=2, ipadx= 143)

# Creating textboxes
f_name = Entry(root, width=30)
f_name.grid(column=1, row=0, padx=20, pady=(10,0))

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

delete_entry = Entry(root, width=30)
delete_entry.grid(column=1, row=9, pady=5)

# Creating textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(column=0, row=0, pady=(10,0))

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

delete_label = Label(root, text="Enter ID")
delete_label.grid(column=0, row=9, pady=5)

# Submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(column=0, row= 6, padx=10, pady=10, columnspan=2, ipadx=98)


# Show button
show_btn = Button(root, text= "Show records", command=show)
show_btn.grid(column=0,row=7, padx=10, pady=10, columnspan=2, ipadx=124)

# Delete button
delete_btn = Button(root, text= "Delete ID", command=delete)
delete_btn.grid(column=0, row=10, padx=10, pady=10, columnspan=2, ipadx= 136)

# Edit button
edit_btn = Button(root, text= "Edit ID", command=edit)
edit_btn.grid(column=0, row=11, padx=10, pady=10, columnspan=2, ipadx= 143)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()