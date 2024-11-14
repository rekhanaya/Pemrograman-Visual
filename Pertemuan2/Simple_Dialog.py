import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()
#the input dialog
Nama = simpledialog.askstring(title="Input",
                              prompt="Masukkan Nama Anda: ")

messagebox.showinfo("showinfo", "Hello " +Nama- + " Selamat datang di UPJ")