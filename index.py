
import tkinter as tk
from tkinter import messagebox, Menu
import csv
import os

# CSV file name
CSV_FILE = "contacts.csv"

# Function to write data to CSV
def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Full Name", "Email Address", "Phone Number", "Address"])
        writer.writerow(data)

# Function to handle submit
def submit_form():
    full_name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    address = entry_address.get().strip()

    if not full_name or not email or not phone or not address:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    save_to_csv([full_name, email, phone, address])
    messagebox.showinfo("Success", "Contact saved successfully.")
    clear_form()

# Function to clear all fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to view contacts CSV
def view_contacts():
    if os.path.exists(CSV_FILE):
        os.system(f'notepad {CSV_FILE}')  # Windows only; use 'open' for macOS
    else:
        messagebox.showinfo("Info", "No contacts file found.")

# Create GUI window
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x350")
root.config(padx=20, pady=20, bg="#f0f8ff")

# Form Labels and Entry Fields
tk.Label(root, text="Full Name:", bg="#f0f8ff").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email Address:", bg="#f0f8ff").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Phone Number:", bg="#f0f8ff").grid(row=2, column=0, sticky="w")
entry_phone = tk.Entry(root, width=40)
entry_phone.grid(row=2, column=1)

tk.Label(root, text="Address:", bg="#f0f8ff").grid(row=3, column=0, sticky="w")
entry_address = tk.Entry(root, width=40)
entry_address.grid(row=3, column=1)

# Submit and Clear buttons
tk.Button(root, text="Submit", width=15, bg="green", fg="white", command=submit_form).grid(row=4, column=0, pady=20)
tk.Button(root, text="Clear", width=15, bg="red", fg="white", command=clear_form).grid(row=4, column=1, pady=20)

# Menu Bar
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="View Contacts", command=view_contacts)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()
