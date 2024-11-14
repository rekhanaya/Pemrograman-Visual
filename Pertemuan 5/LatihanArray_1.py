#Diketahui array X = [1,2,3,4,5,6,7,8,9,10]
#Diketahui array Y = [2,4,9,16,25,36,49,64,81,100]
#Tampilkan array dalam bentuk grafik

import matplotlib.pyplot as plt

# Array X dan Y
x_axis = [1, 2, -3, 4, -5, 6, 7, -8, 9, 10]
y_axis = [2, 4, 9, -16, 25, -36, 49, 64, -81, 100]

# Menampilkan judul grafik
plt.title("Diagram Kartesius")

# Membuat grafik
plt.scatter(x_axis, y_axis, color="blue", marker='.', label='item 1')

#Membuat garis 0,0 pada sumbu y dan x
plt.axhline(0, color='black')

# Memberi label pada sumbu
plt.xlabel("Nilai X")
plt.ylabel("Nilai Y")

# Menampilkan grid
plt.grid(True)
plt.legend()

# Menampilkan grafik
plt.show()
