import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk

def show_database():
    root = tk.Tk()
    root.title("Table")
    tree = ttk.Treeview(root)
    
    tree["columns"]=("1","2","3", "4", "5", "6", "7", "8")
    tree.column("1", width=70)
    tree.column("2", width=700)
    tree.column("3", width=60)
    tree.column("4", width=70)
    tree.column("5", width=70)
    tree.column("6", width=70)
    tree.column("7", width=70)
    tree.column("8", width=100)
    tree.heading("1", text="seller")
    tree.heading("2", text="items")
    tree.heading("3", text="quantity")
    tree.heading("4", text="bought")
    tree.heading("5", text="CAD")
    tree.heading("6", text="rank")
    tree.heading("7", text="ASIN")
    tree.heading("8", text="UPS")
    tree.pack_propagate(0)
    
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Androwmaged3030",
        database="amazon"
        )
    # Retrieve data from the table
    cursor = cnx.cursor()
    query = "SELECT seller, item, quantity, priceboughtCAD, pricesellingCAD, Ran, ASIN, UPC FROM seller"



    cursor.execute(query)
    # Insert data into the treeview
    for row in cursor:
        tree.insert("", "end", values=row)
    tree.pack()
    root.mainloop()
    pass

def show_specific_database(Name):
    root = tk.Tk()
    root.title("Table")
    tree = ttk.Treeview(root)

    tree["columns"]=("1","2","3", "4", "5", "6", "7", "8")
    tree.column("1", width=70)
    tree.column("2", width=700)
    tree.column("3", width=60)
    tree.column("4", width=70) 
    tree.column("5", width=70)
    tree.column("6", width=70)
    tree.column("7", width=70)
    tree.column("8", width=100)
    tree.heading("1", text="seller")
    tree.heading("2", text="items")
    tree.heading("3", text="quantity")
    tree.heading("4", text="bought")
    tree.heading("5", text="CAD")
    tree.heading("6", text="rank")
    tree.heading("7", text="ASIN")
    tree.heading("8", text="UPS")
    tree.pack_propagate(0)
    
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Androwmaged3030",
        database="amazon"
        )
    # Retrieve data from the table
    cursor = cnx.cursor()
    query = "SELECT seller, item, quantity, priceboughtCAD, pricesellingCAD, Ran, ASIN, UPC FROM seller"



    cursor.execute(query)
    # Insert data into the treeview
    for row in cursor:
        tree.insert("", "end", values=row)
    tree.pack()
    root.mainloop()
    
def show_add_screen():
    root = tk.Tk()
    frame3 = tk.Frame(root)
    frame3.pack()
    # Entry for seller
    seller_label = tk.Label(frame3, text="Seller:")
    seller_label.pack(side='top')
    seller_entry = tk.Entry(frame3, width=90)
    seller_entry.pack(side='top')

    # Entry for item
    item_label = tk.Label(frame3, text="Item:")
    item_label.pack(side='top')
    item_entry = tk.Entry(frame3, width=90)
    item_entry.pack(side='top')

    # Entry for quantity
    quantity_label = tk.Label(frame3, text="Quantity:")
    quantity_label.pack(side='top')
    quantity_entry = tk.Entry(frame3, width=90)
    quantity_entry.pack(side='top')

    # Entry for priceboughtCAD
    priceboughtCAD_label = tk.Label(frame3, text="Price Bought (CAD):")
    priceboughtCAD_label.pack(side='top')
    priceboughtCAD_entry = tk.Entry(frame3, width=90)
    priceboughtCAD_entry.pack(side='top')

    # Entry for pricesellingCAD
    pricesellingCAD_label = tk.Label(frame3, text="Price Selling (CAD):")
    pricesellingCAD_label.pack(side='top')
    pricesellingCAD_entry = tk.Entry(frame3, width=90)
    pricesellingCAD_entry.pack(side='top')

    # Entry for Ran
    Ran_label = tk.Label(frame3, text="Rank:")
    Ran_label.pack(side='top')
    Ran_entry = tk.Entry(frame3, width=90)
    Ran_entry.pack(side='top')

    # Entry for ASIN
    ASIN_label = tk.Label(frame3, text="ASIN:")
    ASIN_label.pack(side='top')
    ASIN_entry = tk.Entry(frame3, width=90)
    ASIN_entry.pack(side='top')

    # Entry for UPS
    UPS_label = tk.Label(frame3, text="UPS:")
    UPS_label.pack(side='top')
    UPS_entry = tk.Entry(frame3, width=90)
    UPS_entry.pack(side='top')

    # Add item button
    add_item_button = tk.Button(frame3, text="Add Item")
    add_item_button.pack(side='top', anchor='center')
    

root = tk.Tk()
root.geometry("700x700") # Set the width to 500 and height to 500
root.title("Database App")

frame2 = tk.Frame(root)
frame2.pack()

entry = tk.Entry(frame2, width=90)
entry.pack(side='left')

add_item_button = tk.Button(frame2, text="Enter the name of the seller", command=lambda: show_specific_database(entry.get()))
add_item_button.pack(side='left', anchor='center')

frame1 = tk.Frame(root)
frame1.pack()

text_area = tk.Text(frame1, height=100, width=50)
show_database_button = tk.Button(frame1, text="Show Database", command=show_database)
show_database_button.pack(side='right', padx=20)

frame4 = tk.Frame(root)
frame4.pack()

text_area = tk.Text(frame1, height=100, width=50)
show_database_button = tk.Button(frame4, text="Show Database", command=show_add_screen)
show_database_button.pack(side='right', padx=20)




root.mainloop()
