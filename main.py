import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk

def exit_root(root):
    root.destroy()

def show_database():
    root = tk.Tk()
    root.title("Table")
    root.config(bg='orange')
    tree = ttk.Treeview(root)
    
    tree["columns"]=("1","2","3", "4", "5", "6", "7", "8")
    tree.column("1", width=70)
    tree.column("2", width=700)
    tree.column("3", width=60)
    tree.column("4", width=70)
    tree.column("5", width=70)
    tree.column("6", width=70)
    tree.column("7", width=110)
    tree.column("8", width=130)
    tree.heading("1", text="seller")
    tree.heading("2", text="items")
    tree.heading("3", text="quantity")
    tree.heading("4", text="bought")
    tree.heading("5", text="CAD")
    tree.heading("6", text="rank")
    tree.heading("7", text="ASIN")
    tree.heading("8", text="UPC")
    tree.pack_propagate(0)
    
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="***",
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
    
    entry.delete(0, 'end')
    root = tk.Tk()
    
    root.config(bg='orange')
    root.title("Table")
    tree = ttk.Treeview(root)

    tree["columns"]=("1","2","3", "4", "5", "6", "7", "8")
    tree.column("1", width=70)
    tree.column("2", width=700)
    tree.column("3", width=60)
    tree.column("4", width=70) 
    tree.column("5", width=70)
    tree.column("6", width=70)
    tree.column("7", width=110)
    tree.column("8", width=130)
    tree.heading("1", text="seller")
    tree.heading("2", text="items")
    tree.heading("3", text="quantity")
    tree.heading("4", text="bought")
    tree.heading("5", text="CAD")
    tree.heading("6", text="rank")
    tree.heading("7", text="ASIN")
    tree.heading("8", text="UPC")
    tree.pack_propagate(0)
    
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="***",
        database="amazon"
        )
    # Retrieve data from the table
    cursor = cnx.cursor()
    query = "SELECT seller, item, quantity, priceboughtCAD, pricesellingCAD, Ran, ASIN, UPC FROM seller WHERE seller = %s"
    seller_name = Name
    cursor.execute(query, (seller_name,))
    # Insert data into the treeview
    for row in cursor:
        tree.insert("", "end", values=row)
    tree.pack()
    root.mainloop()
    
def edit_screen():
    root5 = tk.Tk()
    root5.config(bg='orange')
    
    
    frame3 = tk.Frame(root5, bg="#FFA500")
    frame3.pack()

    seller_label1 = tk.Label(frame3, text="Write the name of the Seller and the name UPC of the item and change what you would like to change")
    seller_label1.config(background='orange')
    seller_label1.pack(side='top')

    seller_label = tk.Label(frame3, text="Seller:")
    seller_label.config(background='orange')
    seller_label.pack(side='top')
    seller_entry = tk.Entry(frame3, width=120)
    seller_entry.config(bg="purple", fg="orange")
    seller_entry.pack(side='top')

    # Entry for UPC
    UPC_label = tk.Label(frame3, text="UPC:")
    UPC_label.config(background='orange')
    UPC_label.pack(side='top')
    UPC_entry = tk.Entry(frame3, width=120)
    UPC_entry.config(bg="purple", fg="orange")
    UPC_entry.pack(side='top')
    

    # Entry for quantity
    quantity_label = tk.Label(frame3, text="Quantity:")
    quantity_label.config(background='orange')
    quantity_label.pack(side='top')
    quantity_entry = tk.Entry(frame3, width=120)
    quantity_entry.config(bg="purple", fg="orange")
    quantity_entry.pack(side='top')

    # Entry for priceboughtCAD
    priceboughtCAD_label = tk.Label(frame3, text="Price Bought (CAD):")
    priceboughtCAD_label.config(background='orange')
    priceboughtCAD_label.pack(side='top')
    priceboughtCAD_entry = tk.Entry(frame3, width=120)
    priceboughtCAD_entry.config(bg="purple", fg="orange")
    priceboughtCAD_entry.pack(side='top')

    # Entry for pricesellingCAD
    pricesellingCAD_label = tk.Label(frame3, text="Price Selling (CAD):")
    pricesellingCAD_label.config(background='orange')
    pricesellingCAD_label.pack(side='top')
    pricesellingCAD_entry = tk.Entry(frame3, width=120)
    pricesellingCAD_entry.config(bg="purple", fg="orange")
    pricesellingCAD_entry.pack(side='top')

    # Entry for Ran
    Ran_label = tk.Label(frame3, text="Rank:")
    Ran_label.config(background='orange')
    Ran_label.pack(side='top')
    Ran_entry = tk.Entry(frame3, width=120)
    Ran_entry.config(bg="purple", fg="orange")
    Ran_entry.pack(side='top')

   

    

    # Add item button
    add_item_button = tk.Button(frame3, text="Add Item", command=lambda: edit_item(seller_entry.get(), quantity_entry.get(), priceboughtCAD_entry.get(), pricesellingCAD_entry.get(), Ran_entry.get(), UPC_entry.get(), root5),  bg="orange")
    add_item_button.pack(side='top', anchor='center')
    
def edit_item(seller, quantity, priceboughtCAD, pricesellingCAD, rank, UPC, root5):
    exit_root(root5)
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="***",
        database="amazon"
    )
    cursor = cnx.cursor()
    set_clauses = []
    data = []

    if quantity:
        set_clauses.append("quantity = %s")
        data.append(quantity)
    if priceboughtCAD:
        set_clauses.append("priceboughtCAD = %s")
        data.append(priceboughtCAD)
    if pricesellingCAD:
        set_clauses.append("pricesellingCAD = %s")
        data.append(pricesellingCAD)
    if rank:
        set_clauses.append("Ran = %s")
        data.append(rank)
    

    set_clause_str = ", ".join(set_clauses)
    query = f"UPDATE seller SET {set_clause_str} WHERE seller = %s AND UPC = %s"
    data.extend([seller, UPC])

    cursor.execute(query, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def add_item(seller, item, quantity, priceboughtCAD, pricesellingCAD, rank, ASIN, UPC):
    
    

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="amazon"
        )
        cursor = conn.cursor()

        # Execute the INSERT statement
        cursor.execute("INSERT INTO seller (seller, item, quantity, priceboughtCAD, pricesellingCAD, Ran, ASIN, UPC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (seller, item, quantity, priceboughtCAD, pricesellingCAD, rank, ASIN, UPC))
        conn.commit()

        # Print a success message
        root1 = tk.Tk()
        root1.config(bg='orange')
        root1.geometry("300x100") # Set the width to 100 and height to 100
        
        frame3 = tk.Frame(root1, bg="#FFA500")
        frame3.pack()

        seller_label1 = tk.Label(frame3, text="The item is added succesfully")
        seller_label1.config(background='orange')
        seller_label1.pack(side='top')
        exit_button = tk.Button(frame3, text="OK!",command=lambda: exit_root(root1),  bg="orange")
        exit_button.pack()
        seller_entry.delete(0, 'end')
        item_entry.delete(0, 'end')
        quantity_entry.delete(0, 'end')
        priceboughtCAD_entry.delete(0, 'end')
        pricesellingCAD_entry.delete(0, 'end')
        Ran_entry.delete(0, 'end')
        ASIN_entry.delete(0, 'end')
        UPC_entry.delete(0, 'end')


    except Exception as e:
        # Print an error message
        print("Error inserting data: ", e)
        root2 = tk.Tk()
        root2.config(bg='orange')
        root2.geometry("300x100") # Set the width to 100 and height to 100
        
        frame3 = tk.Frame(root2, bg="#FFA500")
        frame3.pack()

        seller_label1 = tk.Label(frame3, text="Please Make sure you insearted the right data \n make sure there is not white spaces \nor you write a charachter intead of a digit")
        seller_label1.config(background='orange')
        seller_label1.pack(side='top')
        exit_button = tk.Button(frame3, text="Let me take another look!",command=lambda: exit_root(root2),  bg="orange")
        exit_button.pack()

    finally:
        # Close the cursor and the connection
        
        cursor.close()
        conn.close()

    

root = tk.Tk()
root.config(bg='orange')
root.geometry("690x550") # Set the width to 690 and height to 550
root.title("Database App")



frame3 = tk.Frame(root)
frame3.pack( anchor='nw')

image = Image.open("amazon.jpg")
image.thumbnail((100,100))
image.save("amazon.jpg")
photo = ImageTk.PhotoImage(image)
# Adding an image to the tkinter window
image = Image.open("your_thumbnail.jpg")

photo = ImageTk.PhotoImage(image)
label = tk.Label(frame3, image=photo)
label.pack(side='left', padx=0)

seller_label = tk.Label(frame3, text="ndrewid", font=("Helvetica", 40), bg="#ffffff", fg='orange')
seller_label.pack(side='left')

seller_label = tk.Label(frame3, text=" - If it does not exist. We are working on it.      ", font=("Times", 16), bg="#ffffff", fg='orange')
seller_label.pack(side='left')

frame2 = tk.Frame(root, bg="#FFA500")
frame2.pack()

seller_label = tk.Label(frame2, text="Seller:", font=("Helvetica", 10), bg="#ffffff")
seller_label.config(background='orange')
seller_label.pack(side='left')
entry = tk.Entry(frame2, width=90)
entry.config(bg="purple", fg="orange")
entry.pack(side='left')


add_item_button = tk.Button(frame2, text="Show seller Itmes", command=lambda: show_specific_database(entry.get()),  bg="orange")
add_item_button.pack(side='left', anchor='center')

frame1 = tk.Frame(root, bg="#FFA500")
frame1.pack()

text_area = tk.Text(frame1, height=100, width=100)
show_database_button = tk.Button(frame1, text="Show Database", command=show_database,  bg="orange")
show_database_button.pack(side='right', padx=20)

text_area = tk.Text(frame1, height=100, width=100)
show_database_button = tk.Button(frame1, text="Edit item", command=edit_screen,  bg="orange")
show_database_button.pack(side='right', padx=20)

frame4 = tk.Frame(root, bg="#FFA500")
frame4.pack(anchor='nw')
seller_label = tk.Label(frame4, text="\n\nAdd an Item")
seller_label.config(background='orange')
seller_label.pack(side='top')      
# Entry for seller
seller_label = tk.Label(frame4, text="Seller:")
seller_label.config(background='orange')
seller_label.pack(side='top')
seller_entry = tk.Entry(frame4, width=120)
seller_entry.config(bg="purple", fg="orange")
seller_entry.pack(side='top')

 # Entry for item
item_label = tk.Label(frame4, text="Item:")
item_label.config(background='orange')
item_label.pack(side='top')
item_entry = tk.Entry(frame4, width=120)
item_entry.config(bg="purple", fg="orange")
item_entry.pack(side='top')

# Entry for quantity
quantity_label = tk.Label(frame4, text="Quantity:")
quantity_label.config(background='orange')
quantity_label.pack(side='top')
quantity_entry = tk.Entry(frame4, width=120)
quantity_entry.config(bg="purple", fg="orange")
quantity_entry.pack(side='top')

# Entry for priceboughtCAD
priceboughtCAD_label = tk.Label(frame4, text="Price Bought (CAD):")
priceboughtCAD_label.config(background='orange')
priceboughtCAD_label.pack(side='top')
priceboughtCAD_entry = tk.Entry(frame4, width=120)
priceboughtCAD_entry.config(bg="purple", fg="orange")
priceboughtCAD_entry.pack(side='top')

# Entry for pricesellingCAD
pricesellingCAD_label = tk.Label(frame4, text="Price Selling (CAD):")
pricesellingCAD_label.config(background='orange')
pricesellingCAD_label.pack(side='top')
pricesellingCAD_entry = tk.Entry(frame4, width=120)
pricesellingCAD_entry.config(bg="purple", fg="orange")
pricesellingCAD_entry.pack(side='top')

# Entry for Ran
Ran_label = tk.Label(frame4, text="Rank:")
Ran_label.config(background='orange')
Ran_label.pack(side='top')
Ran_entry = tk.Entry(frame4, width=120)
Ran_entry.config(bg="purple", fg="orange")
Ran_entry.pack(side='top')

# Entry for ASIN
ASIN_label = tk.Label(frame4, text="ASIN:")
ASIN_label.config(background='orange')
ASIN_label.pack(side='top')
ASIN_entry = tk.Entry(frame4, width=120)
ASIN_entry.config(bg="purple", fg="orange")
ASIN_entry.pack(side='top')

# Entry for UPC
UPC_label = tk.Label(frame4, text="UPC:")
UPC_label.config(background='orange')
UPC_label.pack(side='top')
UPC_entry = tk.Entry(frame4, width=120)
UPC_entry.config(bg="purple", fg="orange")
UPC_entry.pack(side='top')

# Add item button
add_item_button = tk.Button(frame4, text="Add Item", command=lambda: add_item(seller_entry.get(), item_entry.get(), quantity_entry.get(), priceboughtCAD_entry.get(), pricesellingCAD_entry.get(), Ran_entry.get(), ASIN_entry.get(), UPC_entry.get()),  bg="orange")
add_item_button.pack(side='top', anchor='center')



root.mainloop()
