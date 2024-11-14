#Combo jenis barang

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Membuat jendela utama
root = Tk()
root.title("Latihan Combo")
root.geometry('800x150')

# Data jenis barang yang tersedia
jenis_barang = ["Laptop", "Gadget", "Server"]

# Fungsi untuk mengubah opsi merek berdasarkan jenis barang yang dipilih
def update_merek_options(event):
    # Mendapatkan indeks jenis barang yang dipilih
    selected_index = jenis_barang_combo.current()
    # Mengupdate field index dengan indeks yang dipilih
    index_entry.delete(0, END)
    index_entry.insert(0, str(selected_index))

    # Mendapatkan jenis barang yang dipilih
    selected_jenis_barang = jenis_barang_combo.get()
    # Mengatur opsi merek sesuai dengan jenis barang yang dipilih
    if selected_jenis_barang == "Laptop":
        merek_combo['values'] = ["Asus", "Dell", "HP", "Lenovo", "Acer"]
    elif selected_jenis_barang == "Gadget":
        merek_combo['values'] = ["Samsung", "Apple", "Xiaomi", "Infinix", "Vivo", "OPPO"]
    elif selected_jenis_barang == "Server":
        merek_combo['values'] = ["Dell", "HP", "IBM", "Cisco"]
    else:
        merek_combo['values'] = []

    # Mengupdate field selected item dengan jenis barang yang dipilih
    selected_item_entry.delete(0, END)
    selected_item_entry.insert(0, selected_jenis_barang)

# Fungsi untuk menampilkan pesan dengan data jenis barang dan merek yang dipilih
def show_message():
    selected_jenis_barang = jenis_barang_combo.get()
    selected_merek = merek_combo.get()
    messagebox.showinfo("Data Barang", f"Jenis Barang: {selected_jenis_barang}\nMerek: {selected_merek}")

# Membuat label untuk jenis barang
lbl_jenis_barang = Label(root, text="Jenis Barang", font=("bold", 10))
lbl_jenis_barang.place(x=20, y=10)

# Membuat combo box untuk jenis barang
jenis_barang_combo = Combobox(root, values=jenis_barang)
jenis_barang_combo.place(x=120, y=10)
jenis_barang_combo.bind("<<ComboboxSelected>>", update_merek_options)

# Membuat field untuk index
index_entry = Entry(root)
index_entry.place(x=350, y=10)

# Membuat field untuk selected item
selected_item_entry = Entry(root)
selected_item_entry.place(x=590, y=10)

# Membuat label untuk merek
lbl_merek = Label(root, text="Merek", font=("bold", 10))
lbl_merek.place(x=20, y=50)

# Membuat combo box untuk merek
merek_combo = Combobox(root, values=[])
merek_combo.place(x=120, y=50)

# Membuat tombol "OK" untuk menampilkan pesan
btn_ok = Button(root, text="OK", command=show_message)
btn_ok.place(x=300, y=50)

# Menjalankan program
root.mainloop()
