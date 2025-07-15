
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(host="localhost", user="root", password="", database="billing_db")
cursor = conn.cursor()

# Colors
bg_color = "#f0f0f0"
header_color = "#344955"
btn_color = "#4a6572"
text_color = "#ffffff"

# Main Window
root = tk.Tk()
root.title("Billing Software")
root.geometry("800x600")
root.configure(bg=bg_color)

# Add Logo/Image
logo_img = Image.open("logo.png")  # Use your image file here
logo_img = logo_img.resize((80, 80))
logo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(root, image=logo, bg=bg_color)
logo_label.place(x=10, y=10)

# Header
header = tk.Label(root, text="Billing Management System", bg=header_color, fg=text_color,
                  font=("Helvetica", 20, "bold"), pady=10)
header.pack(fill=tk.X)

# Product Frame
frame = tk.Frame(root, bg=bg_color)
frame.place(x=50, y=120)

tk.Label(frame, text="Product ID:", bg=bg_color).grid(row=0, column=0, padx=10, pady=5)
tk.Label(frame, text="Quantity:", bg=bg_color).grid(row=1, column=0, padx=10, pady=5)

entry_product_id = tk.Entry(frame)
entry_quantity = tk.Entry(frame)
entry_product_id.grid(row=0, column=1, pady=5)
entry_quantity.grid(row=1, column=1, pady=5)

# TreeView for invoice
tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Qty", "Total"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
tree.place(x=50, y=250, width=700, height=250)

def add_to_invoice():
    pid = entry_product_id.get()
    qty = entry_quantity.get()
    if not pid or not qty:
        messagebox.showwarning("Input error", "All fields are required.")
        return
    try:
        cursor.execute("SELECT name, price, stock FROM products WHERE id = %s", (pid,))
        product = cursor.fetchone()
        if product:
            name, price, stock = product
            qty = int(qty)
            if qty > stock:
                messagebox.showerror("Stock error", "Insufficient stock.")
                return
            total = price * qty
            cursor.execute("INSERT INTO invoices (product_id, quantity, total) VALUES (%s, %s, %s)", (pid, qty, total))
            cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (qty, pid))
            conn.commit()
            tree.insert("", "end", values=(pid, name, price, qty, total))
        else:
            messagebox.showerror("Product not found", "No such product ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

btn_add = tk.Button(root, text="Add to Invoice", command=add_to_invoice,
                    bg=btn_color, fg=text_color, font=("Helvetica", 12, "bold"))
btn_add.place(x=300, y=200)

root.mainloop()
