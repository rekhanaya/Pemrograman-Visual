#Latihan Combo 1

# Import modul tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox

# Membuat jendela utama
root = Tk()

# Memberikan judul pada jendela
root.title("Latihan Combo")

# Menentukan ukuran jendela
root.geometry('300x300')

# Membuat label untuk menampilkan teks "Prodi"
lbl = Label(root, text="Prodi", font=("bold", 10))
lbl.place(x=20, y=10)

# Membuat combo box (kotak kombinasi) dengan pilihan prodi
combo = Combobox(root, values=["DKV", "DP", "INF", "SIF", "TSP", "ARS"])
combo.place(x=70, y=10)

# Fungsi yang akan dipanggil saat pilihan dalam combo box berubah
def option_selected(event):
    selected_option = combo.get()  # Mendapatkan opsi yang dipilih dari combo box
    print("Prodi Anda: ", selected_option)  # Mencetak opsi yang dipilih ke konsol
    # Menampilkan pesan dialog dengan opsi yang dipilih
    msg = messagebox.showinfo("Prodi", "Prodi Anda: " + selected_option)

# Mengikat fungsi option_selected ke peristiwa "ComboboxSelected" (pilihan dalam combo box berubah)
combo.bind("<<ComboboxSelected>>", option_selected)

# Memulai event loop Tkinter
root.mainloop()
