#Nama : Rekha Inaya Putri
#NIM : 2022071044
#Soal: Membuat program GUI untuk menghasilkan gambar bunga

import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah(domain) diagram cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-8,8,10000)
plt.figure(figsize=(8,6.5))

#Menentukan persamaan matematika y untuk setiap lingkaran
y = x -x -0
y1 = (20-(x-0)**2)**0.5
y2 = 0 - (20-(x-0)**2)**0.5

y3 = 6 + (4-(x+0)**2)**0.5
y4 = 6 - (4-(x+0)**2)**0.5

y5 = -6 + (4-(x-0)**2)**0.5
y6 = -6 - (4-(x-0)**2)**0.5

y7 = 0 + (4-(x-6)**2)**0.5
y8 = 0 - (4-(x-6)**2)**0.5

y9 = 0 + (4-(x+6)**2)**0.5
y10 = 0 - (4-(x+6)**2)**0.5

y11 = 4 + (4-(x-4)**2)**0.5
y12 = 4 - (4-(x-4)**2)**0.5

y13 = -4 + (4-(x-4)**2)**0.5
y14 = -4 - (4-(x-4)**2)**0.5

y15 = 4 + (4-(x+4)**2)**0.5
y16 = 4 - (4-(x+4)**2)**0.5

y17 = -4 + (4-(x+4)**2)**0.5
y18 = -4 - (4-(x+4)**2)**0.5

#Membuat warna tepi pada lingkaran dan label
plt.plot(x, y, 'none')
plt.plot(x, y1, 'r', label='bunga')
plt.plot(x, y2, 'r')
plt.plot(x, y3, 'b')
plt.plot(x, y4, 'b')
plt.plot(x, y5, 'b')
plt.plot(x, y6, 'b')
plt.plot(x, y7, 'b')
plt.plot(x, y8, 'b')
plt.plot(x, y9, 'b')
plt.plot(x, y10, 'b')
plt.plot(x, y11, 'b')
plt.plot(x, y12, 'b')
plt.plot(x, y13, 'b')
plt.plot(x, y14, 'b')
plt.plot(x, y15, 'b')
plt.plot(x, y16, 'b')
plt.plot(x, y17, 'b')
plt.plot(x, y18, 'b')

#Menambahkan warna di dalam lingkaran
plt.fill_between(x, y1, y2, color='pink', alpha=0.9)
plt.fill_between(x, y3, y4, color='magenta')
plt.fill_between(x, y5, y6, color='magenta')
plt.fill_between(x, y7, y8, color='magenta')
plt.fill_between(x, y9, y10, color='magenta')
plt.fill_between(x, y11, y12, color='magenta')
plt.fill_between(x, y13, y14, color='magenta')
plt.fill_between(x, y15, y16, color='magenta')
plt.fill_between(x, y17, y18, color='magenta')

#Menampilkan grafik
plt.legend(loc='upper left')
plt.grid()
plt.show()
