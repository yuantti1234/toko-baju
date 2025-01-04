import tkinter as tk
from tkinter import messagebox

def calculate_price():
    item = item_var.get()
    size = size_var.get()

    # Harga berdasarkan item dan ukuran
    price_list = {
        "Celana": {"S": 50000, "M": 60000, "L": 70000, "XL": 80000},
        "Baju": {"S": 40000, "M": 50000, "L": 60000, "XL": 70000},
        "Kemeja": {"S": 70000, "M": 80000, "L": 90000, "XL": 100000},
        "Sweater": {"S": 100000, "M": 110000, "L": 120000, "XL": 130000},
    }

    if item and size:
        price = price_list[item][size]
        messagebox.showinfo("Harga", f"Harga {item} ukuran {size}: Rp {price}")
    else:
        messagebox.showwarning("Peringatan", "Pilih item dan ukuran terlebih dahulu!")

# GUI
root = tk.Tk()
root.title("Penjualan Pakaian - Tokoh Arfabi")
root.geometry("400x300")

# Label untuk nama toko
tk.Label(root, text="Tokoh Arfabi", font=("Arial", 16, "bold")).pack(pady=10)

# Dropdown pilihan item
tk.Label(root, text="Pilih Item:").pack()
item_var = tk.StringVar()
item_dropdown = tk.OptionMenu(root, item_var, "Celana", "Baju", "Kemeja", "Sweater")
item_dropdown.pack()

# Dropdown pilihan ukuran
tk.Label(root, text="Pilih Ukuran:").pack()
size_var = tk.StringVar()
size_dropdown = tk.OptionMenu(root, size_var, "S", "M", "L", "XL")
size_dropdown.pack()

# Tombol untuk menghitung harga
calculate_button = tk.Button(root, text="Hitung Harga", command=calculate_price)
calculate_button.pack(pady=20)

# Tombol keluar
exit_button = tk.Button(root, text="Keluar", command=root.destroy)
exit_button.pack()

# Main loop
root.mainloop()
