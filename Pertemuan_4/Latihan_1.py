print("\033c")

import matplotlib.pyplot as plt
import numpy as np

# tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-10, 10, 1000)
plt.figure(figsize = (3, 30))

#gambar lingkaran kecil (titik) pada (0,0)
plt.plot(x, (0.05-x**2)**0.5,       '-k')
plt.plot(x, -((0.05-x**2)**0.5),    '-k')

#Membuat garis 0,0 pada sumbu y dan x
plt.axhline(0, color='blue')

# Menghitung nilai y untuk setiap nilai x
y = x - x - 0
y1 = x**2 + 2*x - 4
y2 = 1/2*x-3


plt.plot(x, y,      '-k')
plt.plot(x, y1,     '-b', label = 'y1')
plt.plot(x, y2,      '-y')

plt.legend(loc='upper left')
plt.grid()
plt.show()