import mysql.connector

#buat object koneksi nama cn
cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)
if(cn.is_connected()):
    print("Server Database telah terhubung")

myCurr = cn.cursor()
myCurr.execute("use MyUpj")
uid = int(input("Id: "))
namaUser = input("Nama User: ")
namaLengkap = input("Nama Lengkap: ")
passwd = input("Password: ")

#buat databse myUPJ
qry = 'INSERT INTO userTable(userld,userName,Password,NamaLengkap) VALUES (%,%,%,%)'
val=(uid,namaUser,passwd,namaLengkap)
#Eksekusi query show database memlalui cursor
myCurr.execute(qry,val)
myCurr.execute("select * from userTable")
for dtb in myCurr:
    print(dtb)
cn.close