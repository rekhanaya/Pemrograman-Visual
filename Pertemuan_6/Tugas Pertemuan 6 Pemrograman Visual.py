#Nama           : Rekha Inaya Putri
#NIM            : 2022071044

from tkinter import *

def konversi_ke_biner():
  # Mendapatkan bilangan desimal
  bilangan_desimal = int(entry_desimal.get())

  # Inisialisasi variabel
  hasil_biner = ""
  while bilangan_desimal > 0:
    sisa = bilangan_desimal % 2
    hasil_biner = str(sisa) + hasil_biner  # Tambahkan sisa ke awal string
    bilangan_desimal //= 2  # Bagi bilangan desimal dengan 2

  # Menampilkan hasil biner
  label_biner.config(text=f"Bilangan Biner: {hasil_biner}")

# Membuat jendela
window = Tk()
window.title("Konversi Desimal ke Biner")

# Membuat label
label_desimal = Label(text="Bilangan Desimal: ")
label_biner = Label(text="Bilangan Biner: ")

# Membuat entry box
entry_desimal = Entry()

# Membuat tombol
button_konversi = Button(text="Konversi", command=konversi_ke_biner)

# Menata layout
label_desimal.grid(row=0, column=0)
entry_desimal.grid(row=0, column=1)
button_konversi.grid(row=1, column=0)
label_biner.grid(row=1, column=1)

# Menjalankan loop window
window.mainloop()
