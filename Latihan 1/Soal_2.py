#Nama: Rekha Inaya Putri
#NIM: 2022071044
#Buatlah program luas dan keliling segitiga dengan menggunakan simple dialog dan massagebox

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()  
ROOT.withdraw()

#Input dialog
sisi=simpledialog.askstring(title="input", prompt="Masukan sisi segitiga:")
alas=simpledialog.askstring(title="input", prompt="Masukan alas segitiga:")
tinggi=simpledialog.askstring(title="input", prompt="Masukan tinggi segitiga:")

#Mengkonversi luas persegi panjang
luas = 0.5*int(alas)*int(tinggi)
ket1="Hasil luas segitiga, dengan alas {0} dan tinggi {1} adalah {2}".format(alas, tinggi, luas)
keliling = 3*int(sisi)
ket2="Hasil keliling segitiga, dengan sisi {0} adalah {1}".format(sisi, keliling)


#menampilkan hasil penjumlahan
messagebox.showinfo("showinfo", ket1)
messagebox.showinfo("showinfo", ket2)