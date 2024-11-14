#Nama: Rekha Inaya Putri
#NIM: 2022071044
#Buatlah program luas dan keliling lingkaran dengan menggunakan simple dialog dan massagebox

import math
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()  
ROOT.withdraw()

#Input dialog
jari=simpledialog.askstring(title="input", prompt="Masukan jari-jari lingkaran:")

#Mengkonversi luas persegi panjang
luas = math.pi*int(jari)*int(jari)
ket1="Hasil luas lingkaran, dengan jari-jari {0} adalah {1}".format(jari, luas)
keliling = 2*math.pi*int(jari)
ket2="Hasil keliling lingkaran, dengan jari-jari {0} adalah {1}".format(jari, keliling)


#menampilkan hasil penjumlahan
messagebox.showinfo("showinfo", ket1)
messagebox.showinfo("showinfo", ket2)