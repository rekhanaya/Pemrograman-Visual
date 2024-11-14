# Membuat bendera indonesia menggunakan grafik

import matplotlib.pyplot as plt
import numpy as np

# Rentang x dan y
x_range = (0, 1200)
y_range = (0, 700)

# Lebar dan tinggi bendera
lebar_bendera = np.arange(300, 1001)
tinggi_merah = np.arange(200, 401)
tinggi_putih = np.arange(401, 601)

# Membuat grid untuk plotting
X, Y = np.meshgrid(np.arange(x_range[0], x_range[1] + 1), np.arange(y_range[0], y_range[1] + 1))

# Inisialisasi array dengan nilai hitam (0, 0, 0)
bendera = np.zeros((y_range[1] + 1, x_range[1] + 1, 3), dtype=np.uint8)

# Menerapkan merah pada area yang sesuai
bendera[(Y >= tinggi_merah[0]) & (Y <= tinggi_merah[-1]) & (X >= lebar_bendera[0]) & (X <= lebar_bendera[-1])] = (255, 0, 0)

# Menerapkan putih pada area yang sesuai
bendera[(Y >= tinggi_putih[0]) & (Y <= tinggi_putih[-1]) & (X >= lebar_bendera[0]) & (X <= lebar_bendera[-1])] = (255, 255, 255)

# Menampilkan grafik
plt.imshow(bendera)
plt.axis('on')  
# Menghilangkan sumbu
plt.show()