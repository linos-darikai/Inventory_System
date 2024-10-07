import random
from tkinter import ttk, messagebox
import csv 

numeric = "0123456789"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"






def read_to_list():
    filename = "database.csv"
    error = [[0, 0,0,0 ,0,0,0]]
    try:
        
        with open(filename, newline = "") as csvfile:
            data = csv.reader(csvfile)
            data = list(data)
        return data
    except FileNotFoundError:
        with open(filename, "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(error)
        return error


   

# Dummy data
dummydata = read_to_list()
for a in dummydata:
    a[2] = float(a[2])
    a[6] = float(a[6])
    a[3] = int(a[3])


def generate_item_id():
    item_id = ""
    for s in range(3):
        item_id += random.choice(numeric)
    for l in range(3):
        item_id += random.choice(alpha)
    return item_id

def remove_inventrory():
    pass

def save():
    pass
def save_to_file(data):
    filename = "database.csv"
    
    
    try:
        with open(filename ,"w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    except FileNotFoundError:
        print("File not Found")



   

            


def search():
    pass

def update():
    pass

def refresh():
    pass

def countItems():
    count = len(dummydata)
    messagebox.showinfo("Item Count", f"Total items: {count}")