import tkinter as tk  # Mengimpor modul tkinter dengan alias 'tk'
from tkinter import Button, Label, Tk  # Mengimpor beberapa kelas yang diperlukan dari modul tkinter

base = Tk()  # Membuat objek utama Tkinter yang akan menjadi jendela aplikasi
base.geometry('450x200')  # Menetapkan ukuran jendela aplikasi
base.title("Latihan Mengubah Tulisan")  # Menetapkan judul jendela aplikasi

def ubahText():  # Mendefinisikan fungsi untuk mengubah teks pada label
    if lbl["text"] == "Hallo UPJ belajar Pemrograman Visual":  # Memeriksa apakah teks label saat ini adalah "Hallo UPJ belajar Pemrograman Visual"
        lbl["text"] = "Tulisan ini diubah menggunakan button!! Semangat coding"  # Mengubah teks label jika kondisi terpenuhi
    else:
        lbl["text"] = "Hallo UPJ belajar Pemrograman Visual"  # Mengembalikan teks label ke nilai awal jika kondisi tidak terpenuhi

lbl = Label(base, text="Hallo UPJ belajar Pemrograman Visual", width=50, font=("bold",10))  # Membuat label dengan teks awal "Hallo UPJ belajar Pemrograman Visual"
lbl.place(x=50, y=50)  # Menempatkan label di koordinat (50, 50) di dalam jendela aplikasi

btn = Button(base, text="Ubah Tulisan", command=ubahText)  # Membuat tombol dengan teks "Ubah Tulisan" yang akan memanggil fungsi ubahText() ketika ditekan
btn.place(x=160, y=100)  # Menempatkan tombol di koordinat (160, 100) di dalam jendela aplikasi

exit_btn = Button(base, text="Exit", command=base.destroy)  # Membuat tombol dengan teks "Exit" yang akan menghancurkan jendela aplikasi (menutup aplikasi) ketika ditekan
exit_btn.place(x=160, y=150)  # Menempatkan tombol "Exit" di bawah tombol "Ubah Tulisan"

base.mainloop()  # Memulai loop utama untuk menjalankan aplikasi Tkinter dan menunggu peristiwa (event) untuk diolah
