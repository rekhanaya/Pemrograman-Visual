#Nama: Rekha Inaya Putri
#NIM: 2022071044
#Buatlah program luas dan keliling persegi panjang dengan menggunakan simple dialog dan massagebox

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()  
ROOT.withdraw()

#Input dialog
panjang=simpledialog.askstring(title="input", prompt="Masukan panjang persegi panjang:")
lebar=simpledialog.askstring(title="input", prompt="Masukan lebar persegi panjang:")

#Mengkonversi luas persegi panjang
luas = int(panjang)*int(lebar)
ket1="Hasil luas persegi panjang, dengan panjang {0} dan lebar {1} adalah {2}".format(panjang, lebar, luas)
keliling = 2*int(panjang) + 2*int(lebar)
ket2="Hasil keliling persegi panjang, dengan panjang {0} dan lebar {1} adalah {2}".format(panjang, lebar, keliling)

#menampilkan hasil penjumlahan
messagebox.showinfo("showinfo", ket1)
messagebox.showinfo("showinfo", ket2)