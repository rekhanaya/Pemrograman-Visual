import tkinter as tk

# program gui tkinter untuk login 

import mysql.connector
from tkinter import *
from tkinter import messagebox

# Membuat koneksi ke server MySQL
cn = mysql.connector.connect(host="localhost", user="root", password="", database="myupj", port=3307)

# Membuat objek cursor untuk berinteraksi dengan database
myCurr = cn.cursor()

# Fungsi untuk melakukan login
def login():
    # Mendapatkan nilai dari field input
    nama_user = nama_user_entry.get()
    passwd = password_entry.get()

    # Mengeksekusi query SQL untuk memeriksa kredensial pengguna
    qry = "SELECT * FROM userTable WHERE UserName = %s AND Password = %s"
    val = (nama_user, passwd)
    myCurr.execute(qry, val)
    result = myCurr.fetchone()

    if result:
        # Menampilkan pesan selamat datang jika kredensial cocok
        messagebox.showinfo("Selamat Datang", f"Selamat datang, {nama_user}!")
    else:
        # Menampilkan pesan kesalahan jika kredensial tidak cocok
        messagebox.showerror("Kesalahan", "Nama pengguna atau kata sandi salah!")

# Membuat jendela utama Tkinter
root = Tk()
root.title("Login")

# Membuat field input
nama_user_label = Label(root, text="Nama User: ")
nama_user_label.grid(row=0, column=0, padx=10, pady=5)
nama_user_entry = Entry(root)
nama_user_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = Label(root, text="Password: ")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Tombol untuk melakukan login
login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Menjalankan loop peristiwa Tkinter
root.mainloop()

# Menutup koneksi database
cn.close()