# buatkan program tkinter menggunakan python menampilkan button:
# Click Me!!
# Jika di click maka akan menampilkan tulisan: "MessageBox : Halo Saya nama_mhs"

import tkinter as tk  # Mengimpor modul tkinter dengan alias 'tk'
from tkinter import Button, Tk, messagebox  # Mengimpor beberapa kelas dan fungsi yang diperlukan dari modul tkinter

base = Tk()  # Membuat objek utama Tkinter yang akan menjadi jendela aplikasi
base.geometry('200x200')  # Menetapkan ukuran jendela aplikasi
base.title("Button Click Me")  # Menetapkan judul jendela aplikasi

def helloCallBack():  # Mendefinisikan fungsi untuk menampilkan pesan dialog
    msg=messagebox.showinfo("Message","Hallo nama saya Rekha Inaya Putri")  # Menampilkan pesan dialog menggunakan messagebox

B = Button(base, text="Click Me!!", command=helloCallBack)  # Membuat tombol dengan teks "Click Me!!" yang akan memanggil fungsi helloCallBack() ketika ditekan
B.place(x=50,y=50)  # Menempatkan tombol di koordinat (50, 50) di dalam jendela aplikasi

base.mainloop()  # Memulai loop utama untuk menjalankan aplikasi Tkinter dan menunggu peristiwa (event) untuk diolah
