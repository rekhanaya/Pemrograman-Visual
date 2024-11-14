#Nama: Rekha Inaya Putri
#NIM: 2022071044
#Buatlah program volume kubus dengan menggunakan simple dialog dan massagebox

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()  
ROOT.withdraw()

#Input dialog
sisi=simpledialog.askstring(title="input", prompt="Masukan sisi kubus:")

#Mengkonversi volume kubus
luas = int(sisi)*int(sisi)*int(sisi)
ket="Hasil volume kubus, dengan sisi {0} adalah {1}".format(sisi, luas)

#menampilkan hasil penjumlahan
messagebox.showinfo("showinfo", ket)