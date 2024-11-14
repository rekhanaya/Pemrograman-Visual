#Menentukan apakah bilangannya ganjil atau genap
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()

bilangan=simpledialog.askstring(title="Input", prompt="Masukan Angka bilangan: ")

if bilangan % 2 == 0:
    messagebox.showinfo("showinfo", str(bilangan)+ "Bilangan genap")
else:
    messagebox.showinfo("showinfo", str(bilangan)+ "Bilangan ganjil")


