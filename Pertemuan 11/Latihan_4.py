#Tambah data ke table 
import mysql.connector
#Buat object koneksi bernama cn
cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)

if(cn.is_connected()):
    print("Server Database telah terhubung")

myCurr = cn.cursor()

# Membuat database baru
# myCurr.execute("Create Database MyUpj")

# Use database myupj
myCurr.execute("use MyUpj")

# Ekseskusi query show database melalui cursor
# myCurr.execute("Show Databases")

# Membuat Table
# myCurr.execute("CREATE TABLE userTable(UserId INT(5), UserName VARCHAR(50),"
            #    "Password VARCHAR (50), NamaLengkap VARCHAR (50), primary key(UserId))")

# Memasukkan data kedalam Table
myCurr.execute('INSERT INTO userTable VALUES (1, "Rekha", "upj123", "Rekha Inaya Putri"), (2, "Chan", "upj123", "Chan Tik")')
# myCurr.execute("desc userTable")

myCurr.execute("select * from userTable")
# loop untuk menampilkan database
for dtb in myCurr:
    print(dtb)
cn.close()