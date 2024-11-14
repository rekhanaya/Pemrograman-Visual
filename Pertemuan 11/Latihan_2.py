import mysql.connector
#Buat object koneksi bernama cn
cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)

if(cn.is_connected()):
    print("Server Database telah terhubung")

myCurr = cn.cursor()

# Membuat database baru
myCurr.execute("Create Database MyUpj")

# Ekseskusi query show database melalui cursor
myCurr.execute("Show Databases")

# loop untuk menampilkan database
for dtb in myCurr:
    print(dtb)
cn.close()