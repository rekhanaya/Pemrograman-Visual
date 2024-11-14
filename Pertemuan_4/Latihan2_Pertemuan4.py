#Nama           : Rekha Inaya Putri
#NIM            : 2022071044
#Hari/Tanggal   : Senin, 26 Februari 2024
#Soal           : Tuliskan persamaan matematika untuk kurva tersebut. 
#Jawab = (x - 2)(-x + 1)(x + 1) = (x - 2)(1 - x**2) = x - x**3 - 2 + 2*x**2 = -x**3 + 2*x**2 + x - 2

print("\033c")

import matplotlib.pyplot as plt
import numpy as np

# tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-3, 3, 10000)
plt.figure(figsize = (3, 30))

#gambar lingkaran kecil (titik) pada (0,0)
plt.plot(x, (0.01-x**2)**0.5,       '-k')
plt.plot(x, -((0.01-x**2)**0.5),    '-k')

# Menghitung nilai y untuk setiap nilai x
y = x-x-0
y1 = -x**3 + 2*x**2 + x - 2


plt.plot(x, y,      '-k')


plt.plot(x, y1,     '-r', label = 'y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()