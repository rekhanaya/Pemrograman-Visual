# Membuat rentang nilai menggunakan message box

import tkinter as tk
from tkinter import messagebox

def show_message():
  nilai = int(nilai_entry.get())
  if nilai >= 80:
    message = "Anda mendapatkan nilai A"
  elif nilai >= 68:
    message = "Anda mendapatkan nilai B"
  elif nilai >= 56:
    message = "Anda mendapatkan nilai C"
  elif nilai >= 45:
    message = "Anda mendapatkan nilai D"
  else:
    message = "Anda mendapatkan nilai E"
  tk.messagebox.showinfo("Nilai", message)

# Membuat jendela
window = tk.Tk()
window.title("Rentang Nilai")

# Membuat label
label_nilai = tk.Label(text="Masukkan Nilai Anda: ")
label_nilai.pack()

# Membuat entry box
nilai_entry = tk.Entry()
nilai_entry.pack()

# Membuat button
button_show = tk.Button(text="Tampilkan", command=show_message)
button_show.pack()

# Menjalankan loop window
window.mainloop()
