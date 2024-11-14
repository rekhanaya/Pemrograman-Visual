import mysql.connector

#Buat object koneksi nama cn
cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)

if(cn.is_connected()):
    print("KONEKSI BERHASIL")
else:
    print("EROR")
 
