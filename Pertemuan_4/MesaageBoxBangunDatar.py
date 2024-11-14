#Nama           : Rekha Inaya Putri
#NIM            : 2022071044
#Hari/Tanggal   : Jumat, 1 Maret 2024

from BangunDatar import BangunDatar
import tkinter as tk
from tkinter import messagebox

#Membuat objek dari class BangunDatar.py
m = BangunDatar()

#Memanggil method untuk ditampilkan di message box
messagebox.showinfo("Luas Segitiga", f"Luas Segitiga: {m.luasSegitiga(8, 5)}")
messagebox.showinfo("Luas Persegi", f"Luas Persegi: {m.luasPersegi(10)}")
messagebox.showinfo("Keliling Persegi", f"Keliling Persegi: {m.kelilingPersegi(5)}")
messagebox.showinfo("Luas Persegi Panjang", f"Luas Persegi Panjang: {m.luasPesegiPanjang(4, 8)}")
messagebox.showinfo("Keliling Persegi Panjang", f"Keliling Persegi Panjang: {m.kelilingPersegiPanjang(10, 2)}")
messagebox.showinfo("Luas Lingkaran", f"Luas Lingkaran: {m.luasLingkaran(7)}")
messagebox.showinfo("Keliling Lingkaran", f"Keliling Lingkaran: {m.kelilingLingkaran(14)}")

#Jalankan loop utama tkinker
root = tk.Tk
root.withdraw()
root.mainloop()