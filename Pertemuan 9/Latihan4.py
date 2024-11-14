#from tkinter import *  # Mengimpor semua kelas dan fungsi dari modul tkinter
#from tkinter import messagebox  # Mengimpor kelas messagebox dari modul tkinter

#top = Tk()  # Membuat objek utama Tkinter yang akan menjadi jendela aplikasi

#C = Canvas(top, bg="blue", height=250, width=300)  # Membuat objek Canvas dengan latar belakang biru, tinggi 250 piksel, dan lebar 300 piksel
#coord = 10, 50, 240, 210  # Koordinat untuk menggambar busur (arc)
#arc = C.create_arc(coord, start=0, extent=150, fill="red")  # Membuat busur (arc) pada objek Canvas dengan koordinat dan atribut tertentu
#line = C.create_line(10,10,200,200,fill='white')  # Membuat garis pada objek Canvas dari titik (10,10) ke titik (200,200) dengan warna putih
#C.pack()  # Menampilkan objek Canvas di jendela aplikasi

#top.mainloop()  # Memulai loop utama untuk menjalankan aplikasi Tkinter dan menunggu peristiwa (event) untuk diolah

from tkinter import *
from tkinter import messagebox

top = Tk()

C = Canvas(top, bg="white", height=400, width=500)  # Mengubah latar belakang menjadi putih dan ukuran menjadi 400x500 piksel
coord = 50, 100, 450, 350  # Mengubah koordinat busur (arc)
arc = C.create_arc(coord, start=0, extent=150, fill="green")  # Mengubah warna busur menjadi hijau
line = C.create_line(50,50,450,400,fill='blue', width=5)  # Mengubah warna garis menjadi biru dan ketebalan menjadi 5 piksel
C.pack()

top.mainloop()
