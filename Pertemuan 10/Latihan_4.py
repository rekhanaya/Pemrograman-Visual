#Latihan membuat radio

from tkinter import *

# Membuat jendela utama
root = Tk()

# Menentukan ukuran jendela
root.geometry('400x200')

# Memberi judul pada jendela
root.title("Radio dan Checkbox")

# Fungsi untuk memperbarui label berdasarkan pilihan radio button
def update_label():
    if radio_var.get() == 1:
        var1.set("Pria ganteng")
    else:
        var1.set("Wanita cantik")

# Fungsi untuk memperbarui label berdasarkan checkbox yang dipilih
def on_check():
    if Checkbutton1.get() == 1:
        var3.set("Browsing dipilih")
    elif Checkbutton1.get() == 0:
        var3.set("...")
    if Checkbutton2.get() == 1:
        var4.set("Coding dipilih")
    elif Checkbutton2.get() == 0:
        var4.set("...")
    if Checkbutton3.get() == 1:
        var5.set("Reading dipilih")
    elif Checkbutton3.get() == 0:
        var5.set("...")

# Fungsi untuk memeriksa pilihan yang dipilih dan menampilkan hasilnya
def periksa():
    hobi = ""
    if Checkbutton1.get() == 1:
        hobi += "Browsing "
    if Checkbutton2.get() == 1:
        hobi += "Coding "
    if Checkbutton3.get() == 1:
        hobi += "Reading "

    jenis_kelamin = ""
    if radio_var.get() == 1:
        jenis_kelamin = "Pria"
    elif radio_var.get() == 2:
        jenis_kelamin = "Wanita"

    var6.set("Jenis Kelamin: " + jenis_kelamin + ", Hobi: " + hobi)

# Membuat label untuk pemilihan jenis kelamin
var = StringVar()
lblJenisKelamin = Label(root, textvariable=var)
var.set("Jenis Kelamin:")
lblJenisKelamin.place(x=10, y=10)

# Membuat radio button untuk pemilihan jenis kelamin
radio_var = IntVar()
radioPria = Radiobutton(root, text="Pria", value=1, variable=radio_var, command=update_label)
radioPria.place(x=100, y=10)
radioWanita = Radiobutton(root, text="Wanita", value=2, variable=radio_var, command=update_label)
radioWanita.place(x=100, y=30)

# Membuat label untuk menampilkan output dari radio button yang dipilih
var1 = StringVar()
lblOutputJenis = Label(root, textvariable=var1)
var1.set("output radio button")
lblOutputJenis.place(x=200, y=10)

# Membuat label untuk pemilihan hobi
var2 = StringVar()
lblHobi = Label(root, textvariable=var2)
var2.set("Hobi:")
lblHobi.place(x=10, y=60)

# Membuat checkbox untuk pemilihan hobi
Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

button1 = Checkbutton(root, text="Browsing", variable=Checkbutton1, command=on_check)
button1.place(x=100, y=60)

button2 = Checkbutton(root, text="Coding", variable=Checkbutton2, command=on_check)
button2.place(x=100, y=80)

button3 = Checkbutton(root, text="Reading", variable=Checkbutton3, command=on_check)
button3.place(x=100, y=100)

# Membuat label untuk menampilkan status masing-masing checkbox
var3 = StringVar()
lblbutton1 = Label(root, textvariable=var3)
var3.set("...")
lblbutton1.place(x=200, y=60)

var4 = StringVar()
lblbutton2 = Label(root, textvariable=var4)
var4.set("...")
lblbutton2.place(x=200, y=80)

var5 = StringVar()
lblbutton3 = Label(root, textvariable=var5)
var5.set("...")
lblbutton3.place(x=200, y=100)

# Membuat tombol untuk melakukan pengecekan
btnPeriksa = Button(root, text='Periksa', command=periksa)
btnPeriksa.place(x=10, y=160)

# Membuat label untuk menampilkan hasil pengecekan
var6 = StringVar()
lblperiksa = Label(root, textvariable=var6)
var6.set("Hasil periksa")
lblperiksa.place(x=100, y=160)

# Memulai event loop Tkinter
root.mainloop()