import tkinter as tk
from tkinter import ttk, messagebox
import random
import csv
from datetime import datetime;
from utils import *




# Initialize the main window
window = tk.Tk()
window.title("Inventory Management System")
window.geometry("720x640")
window.resizable(False, False)

# Define Treeview
my_tree = ttk.Treeview(window, show="headings")

# Placeholder array
placeholderArray = [tk.StringVar() for _ in range(5)]



def refreshTable(): ## needs fixing here
    for data in my_tree.get_children():
        my_tree.delete(data)
    for index, array in enumerate(dummydata):
        my_tree.insert(parent='', index='end', iid=index, text="", values=array, tag="orow")
        my_tree.tag_configure('orow', background="#EEEEEE")


# function to save the inventory
def save():
    item_id = generate_item_id()
    item_name = nameEntry.get()
    item_price = unit_priceEntry.get()
    item_qnt = qntEntry.get()
    item_cat = categoryCombo.get()
    item_buyprice = buying_priceEntry.get()

    item_date = datetime.now().strftime("%Y-%m-%d")


    if item_id and item_name and item_price and item_qnt and item_cat:
        dummydata.append([item_id, item_name, float(item_price), int(item_qnt), item_cat, item_date, float(item_buyprice)])
        # saving to dict then file 
        
        refreshTable()
        # clear_entries()
        messagebox.showinfo("Success", "Item saved successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")
    save_to_file(dummydata)


def update():
    selected = my_tree.focus()
    if selected:
        values = my_tree.item(selected, 'values')
        item_id = dummydata[int(selected)][0]
        # item_id = itemIdEntry.get()
        item_name = nameEntry.get()
        item_price = unit_priceEntry.get()
        item_qnt = qntEntry.get()
        item_cat = categoryCombo.get()
        item_date = values[5]
        item_buyprice = buying_priceEntry.get()

        if item_id and item_name and item_price and item_qnt and item_cat and item_buyprice:
            dummydata[int(selected)] = [item_id, item_name, float(item_price), int(item_qnt), item_cat, item_date, float(item_buyprice)]
            print(dummydata)
            refreshTable()
            print(dummydata)

            messagebox.showinfo("Success", "Item updated successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields")
    else:
        messagebox.showerror("Error", "Please select an item to update")
    save_to_file(dummydata)


def calculate_profit():
    total = 0
    for a in dummydata:
        unit_prof = float(a[2]) - float(a[6])
        profit = unit_prof * a[3]
        total += profit
    refreshTable()
    messagebox.showinfo("MONEY!!!!!!!!!!!!", f"The total projected profit for this is {total} Cedis")





def remove():
    selected = my_tree.focus()
    if selected:
        dummydata.pop(int(selected))
        
        refreshTable()
        messagebox.showinfo("Success", "Item removed successfully!")
    else:
        messagebox.showerror("Error", "Please select an item to remove")

def search():
    query = nameEntry.get()
    results = [item for item in dummydata if query in item]
    if results:
        for data in my_tree.get_children():
            my_tree.delete(data)
        for index, array in enumerate(results):
            my_tree.insert(parent='', index='end', iid=index, text="", values=array, tag="orow")
            my_tree.tag_configure('orow', background="#EEEEEE")
    else:
        messagebox.showinfo("Search", "No items match your search criteria")
    save_to_file(dummydata)

# Frame for buttons
frame = tk.Frame(window, bg="#005f00")  # Changed from #02577A to a green color
frame.pack()

btnColorGreen = "#007F00"  # Green color for some buttons
btnColorRed = "#FF4C4C"    # Red color for the remove button

manageFrame = tk.LabelFrame(frame, text="")

saveBtn = tk.Button(manageFrame, text="SAVE", width=10, borderwidth=3, bg=btnColorGreen, fg='white', command=save)
updateBtn = tk.Button(manageFrame, text="UPDATE", width=10, borderwidth=3, bg=btnColorGreen, fg='white', command=update)
removeBtn = tk.Button(manageFrame, text="REMOVE", width=10, borderwidth=3, bg=btnColorRed, fg='white', command=remove)
searchBtn = tk.Button(manageFrame, text="SEARCH", width=10, borderwidth=3, bg=btnColorGreen, fg='white',command=search)
refreshBtn = tk.Button(manageFrame, text="REFRESH", width=10, borderwidth=3, bg=btnColorGreen, fg='white', command=refreshTable)
countBtn = tk.Button(manageFrame, text="COUNT", width=10, borderwidth=3, bg=btnColorGreen, fg='white', command=countItems)
profitBtn = tk.Button(manageFrame, text="PROFIT", width=10, borderwidth=3, bg=btnColorGreen, fg='white', command=calculate_profit)# change here

saveBtn.grid(row=0, column=0, padx=5, pady=5)
updateBtn.grid(row=0, column=1, padx=5, pady=5)
removeBtn.grid(row=0, column=2, padx=5, pady=5)
searchBtn.grid(row=0, column=3, padx=5, pady=5)
countBtn.grid(row=0, column=4, padx=5, pady=5)
refreshBtn.grid(row=0, column=5, padx=5, pady=5)
profitBtn.grid(row=0, column=6, padx=5, pady=5)

manageFrame.grid(row=0, column=0, sticky="w", padx=[10, 200], pady=20, ipadx=6)

# Frame for entries
entriesFrame = tk.LabelFrame(frame, text="Form", borderwidth=5)
entriesFrame.grid(row=1, column=0, sticky="w", padx=[10, 200], pady=20, ipadx=6)

# Labels
nameLabel = tk.Label(entriesFrame, text="NAME", anchor="e", width=10)
unit_priceLabel = tk.Label(entriesFrame, text="UNIT PRICE", anchor="e", width=10)
qntLabel = tk.Label(entriesFrame, text="QNT", anchor="e", width=10)
categoryLabel = tk.Label(entriesFrame, text="CATEGORY", anchor="e", width=10)
buying_priceLabel = tk.Label(entriesFrame, text="BUY PRICE", anchor="e", width=10)






nameLabel.grid(row=0, column=0, padx=10)
unit_priceLabel.grid(row=1, column=0, padx=10)
qntLabel.grid(row=2, column=0, padx=10)
categoryLabel.grid(row=3, column=0, padx=10)
buying_priceLabel.grid(row=4, column=0, padx=10)


# Entries
nameEntry = tk.Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
unit_priceEntry = tk.Entry(entriesFrame, width=50, textvariable=placeholderArray[1])
qntEntry = tk.Entry(entriesFrame, width=50, textvariable=placeholderArray[2])
categoryCombo = ttk.Combobox(entriesFrame, width=47, textvariable=placeholderArray[3], values=['drinks', 'toiletry', 'bakery','candy'])
buying_priceEntry = tk.Entry(entriesFrame, width=50, textvariable=placeholderArray[4])


nameEntry.grid(row=0, column=1, padx=5, pady=5)
unit_priceEntry.grid(row=1, column=1, padx=5, pady=5)
qntEntry.grid(row=2, column=1, padx=5, pady=5)
categoryCombo.grid(row=3, column=1, padx=5, pady=5)
buying_priceEntry.grid(row=4, column=1, padx=5, pady=5)





# Treeview columns and headings
my_tree['columns'] = ("Item Id", "Name", "Price", "Quantity", "Category", "Date", "Buy Price")

my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column("Item Id", anchor=tk.W, width=70)
my_tree.column("Name", anchor=tk.W, width=100)
my_tree.column("Price", anchor=tk.W, width=100)
my_tree.column("Quantity", anchor=tk.W, width=70)
my_tree.column("Category", anchor=tk.W, width=70)
my_tree.column("Date", anchor=tk.W, width=70)
my_tree.column("Buy Price", anchor=tk.W, width=70)

my_tree.heading("Item Id", text="Item Id", anchor=tk.W)
my_tree.heading("Name", text="Name", anchor=tk.W)
my_tree.heading("Price", text="Price", anchor=tk.W)
my_tree.heading("Quantity", text="Quantity", anchor=tk.W)
my_tree.heading("Category", text="Category", anchor=tk.W)
my_tree.heading("Date", text="Date", anchor=tk.W)
my_tree.heading("Buy Price", text="Buy Price", anchor=tk.W)

my_tree.tag_configure('orow', background="#EEEEEE")
my_tree.pack()

refreshTable()

window.mainloop()