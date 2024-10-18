import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import database

# Connect to the database
database.connect()

# Function to view all bills
def view_command():
    list_box.delete(0, tk.END)
    for row in database.view():
        list_box.insert(tk.END, row)

# Function to add a bill
def add_command():
    database.insert(bill_number_text.get(), date_text.get(), customer_name_text.get(), amount_text.get(), status_text.get())
    view_command()

# Function to get selected bill
def get_selected_row(event):
    global selected_row
    index = list_box.curselection()[0]
    selected_row = list_box.get(index)
    entry_bill_number.delete(0, tk.END)
    entry_bill_number.insert(tk.END, selected_row[1])
    entry_date.delete(0, tk.END)
    entry_date.insert(tk.END, selected_row[2])
    entry_customer_name.delete(0, tk.END)
    entry_customer_name.insert(tk.END, selected_row[3])
    entry_amount.delete(0, tk.END)
    entry_amount.insert(tk.END, selected_row[4])
    entry_status.delete(0, tk.END)
    entry_status.insert(tk.END, selected_row[5])

# Function to delete a bill
def delete_command():
    database.delete(selected_row[0])
    view_command()

# Function to update a bill
def update_command():
    database.update(selected_row[0], bill_number_text.get(), date_text.get(), customer_name_text.get(), amount_text.get(), status_text.get())
    view_command()

# Tkinter setup
window = tk.Tk()
window.title("Bill Management System")

# Labels and entry fields
tk.Label(window, text="Bill Number").grid(row=0, column=0)
bill_number_text = tk.StringVar()
entry_bill_number = tk.Entry(window, textvariable=bill_number_text)
entry_bill_number.grid(row=0, column=1)

tk.Label(window, text="Date").grid(row=1, column=0)
date_text = tk.StringVar()
entry_date = tk.Entry(window, textvariable=date_text)
entry_date.grid(row=1, column=1)

tk.Label(window, text="Customer Name").grid(row=0, column=2)
customer_name_text = tk.StringVar()
entry_customer_name = tk.Entry(window, textvariable=customer_name_text)
entry_customer_name.grid(row=0, column=3)

tk.Label(window, text="Amount").grid(row=1, column=2)
amount_text = tk.StringVar()
entry_amount = tk.Entry(window, textvariable=amount_text)
entry_amount.grid(row=1, column=3)

tk.Label(window, text="Status").grid(row=0, column=4)
status_text = tk.StringVar()
entry_status = tk.Entry(window, textvariable=status_text)
entry_status.grid(row=0, column=5)

# Listbox and scrollbar
list_box = tk.Listbox(window, height=10, width=50)
list_box.grid(row=2, column=0, rowspan=6, columnspan=4)

scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=2, column=4, rowspan=6)

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
tk.Button(window, text="View All", width=12, command=view_command).grid(row=2, column=5)
tk.Button(window, text="Add Bill", width=12, command=add_command).grid(row=3, column=5)
tk.Button(window, text="Update Bill", width=12, command=update_command).grid(row=4, column=5)
tk.Button(window, text="Delete Bill", width=12, command=delete_command).grid(row=5, column=5)
tk.Button(window, text="Close", width=12, command=window.quit).grid(row=6, column=5)

window.mainloop()
