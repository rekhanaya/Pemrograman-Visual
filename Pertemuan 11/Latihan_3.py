import mysql.connector

# Buat object koneksi bernama cn
cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)

if cn.is_connected():
    print("Server Database telah terhubung")

myCurr = cn.cursor()

# Membuat database baru
myCurr.execute("CREATE DATABASE IF NOT EXISTS MyUpj")
myCurr.execute("USE MyUpj")

# Membuat tabel baru
myCurr.execute("CREATE TABLE IF NOT EXISTS userTable (UserId INT(3), UserName VARCHAR(50), Password VARCHAR(50), NamaLengkap VARCHAR(50), PRIMARY KEY(UserId))")

# Ekseskusi query show database melalui cursor
myCurr.execute("DESC userTable")

# Loop untuk menampilkan struktur tabel
for dtb in myCurr:
    print(dtb)

cn.close()