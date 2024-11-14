import numpy as np

A = np.array(['INF', 'SIF', 'TSP'])
B = np.array([-3, 0, 4, 7])
new_B = B.astype('i')
print(new_B.dtype)

C = np.array([-3, 0, 4, 7])
new_C = B.astype(bool)
print(new_C.dtype)

row = 10
col = 10

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint16)
Gambar_new = np.uint8(Gambar)