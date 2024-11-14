print("\033c")       #To close all
#Import libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time


#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-10,10,1000)
plt.figure(figsize=(4,15))


#Draw a small circle at (0,0)
plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")

#Tentukan persamaan matematika yang diinginkan

y3 = x

plt.plot(x, y3, '-g', label='y3')


plt.legend(loc='upper left')
plt.grid()
plt.show()