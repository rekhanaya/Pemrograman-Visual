#Nama : Rekha Inaya Putri
#NIM : 2022071044
#Soal: Membuat program GUI untuk menghasilkan gambar persegi panjang dengan 2 warna

import matplotlib.pyplot as plt
import numpy as np

#Membuat rentang nilai untuk sumbu x dan sumbu y
x_range = (0, 1300)
y_range = (0, 700)

#Menentukan lebar dan tinggi pada masing masing warna 
lebar = np.arange(300, 1100)
tinggi_birutua = np.arange(200, 300)
tinggi_ungu = np.arange(300, 600)

#Membuat grid 
X, Y = np.meshgrid(np.arange(x_range[0], x_range[1] + 1), np.arange(y_range[0], y_range[1] + 1))

#Menginisialisasi array 
persegi_panjang = np.zeros((y_range[1] + 1, x_range[1] + 1, 3), dtype=np.uint8)

#Membuat warna biru tua pada area yang diminta pada dengan gambar
persegi_panjang[(Y >= tinggi_birutua[0]) & (Y <= tinggi_birutua[-1]) & (X >= lebar[0]) & (X <= lebar[-1])] = (50, 50, 90)

#Membuat warna ungu pada area yang diminta pada dengan gambar
persegi_panjang[(Y >= tinggi_ungu[0]) & (Y <= tinggi_ungu[-1]) & (X >= lebar[0]) & (X <= lebar[-1])] = (90, 65, 195)

# Menampilkan grafik
plt.imshow(persegi_panjang)
plt.axis('on') 
plt.show()