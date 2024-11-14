import tkinter as tk  # Mengimpor modul tkinter dengan alias 'tk'

base = tk.Tk()  # Membuat objek utama Tkinter yang akan menjadi jendela aplikasi
base.geometry('450x200')  # Menetapkan ukuran jendela aplikasi
base.title("Persegi Panjang Calculator")  # Menetapkan judul jendela aplikasi

def hitung_luas_dan_keliling():  # Mendefinisikan fungsi untuk menghitung luas dan keliling persegi panjang
    # Mengambil nilai panjang dan lebar dari input pengguna
    panjang = float(panjang_entry.get())  # Mengambil nilai panjang dari entry widget dan mengonversinya ke tipe data float
    lebar = float(lebar_entry.get())  # Mengambil nilai lebar dari entry widget dan mengonversinya ke tipe data float
    
    # Menghitung luas dan keliling
    luas = panjang * lebar  # Menghitung luas persegi panjang
    keliling = 2 * (panjang + lebar)  # Menghitung keliling persegi panjang
    
    # Menampilkan hasil pada label
    hasil_label.config(text=f"Luas: {luas}, Keliling: {keliling}")  # Mengatur teks label hasil dengan nilai luas dan keliling yang telah dihitung

frame = tk.Frame(base, bg='white', width=400, height=400)  # Membuat frame dengan latar belakang putih
frame.pack(fill=tk.BOTH, expand=True)  # Mengatur frame agar mengisi jendela utama secara keseluruhan

panjang_label = tk.Label(frame, text="Panjang:")  # Membuat label untuk menampilkan teks "Panjang:"
panjang_label.pack()  # Menampilkan label "Panjang:" di dalam frame

panjang_entry = tk.Entry(frame)  # Membuat entry widget untuk pengguna memasukkan nilai panjang
panjang_entry.pack()  # Menampilkan entry widget untuk panjang di dalam frame

lebar_label = tk.Label(frame, text="Lebar:")  # Membuat label untuk menampilkan teks "Lebar:"
lebar_label.pack()  # Menampilkan label "Lebar:" di dalam frame

lebar_entry = tk.Entry(frame)  # Membuat entry widget untuk pengguna memasukkan nilai lebar
lebar_entry.pack()  # Menampilkan entry widget untuk lebar di dalam frame

hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_dan_keliling)  # Membuat tombol "Hitung" yang akan memanggil fungsi hitung_luas_dan_keliling() ketika ditekan
hitung_button.pack()  # Menampilkan tombol "Hitung" di dalam frame

hasil_label = tk.Label(frame, text="")  # Membuat label kosong untuk menampilkan hasil perhitungan luas dan keliling
hasil_label.pack()  # Menampilkan label kosong di dalam frame

exit_button = tk.Button(frame, text="Exit", command=base.destroy)  # Membuat tombol "Exit" yang akan menutup jendela aplikasi saat ditekan
exit_button.pack()  # Menampilkan tombol "Exit" di dalam frame

base.mainloop()  # Memulai loop utama untuk menjalankan aplikasi Tkinter dan menunggu peristiwa (event) untuk diolah
