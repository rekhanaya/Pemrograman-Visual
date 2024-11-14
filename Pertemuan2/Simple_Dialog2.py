import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()  
ROOT.withdraw()

# the input dialog
angka1=simpledialog.askstring(title="input", prompt="Masukan Angka 1:")
angka2=simpledialog.askstring(title="input", prompt="Masukan Angka 2:")

#Mengkonversi angka lalu menjumlahkan
sum=int(angka1)+int(angka2)
ket="Hasil penjumlahan {0} dan {1} adalah {2}".format(angka1, angka2, sum)
#menampilkan hasil penjumlahan
messagebox.showinfo("showinfo", ket)