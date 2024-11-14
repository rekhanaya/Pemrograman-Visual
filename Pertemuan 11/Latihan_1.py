import mysql.connector

cn = mysql.connector.connect(host="localhost", user="root", password="", port=3307)

if (cn.is_connected()):
    print("Server telah terhubung")



mycurr = cn.cursor()
mycurr.execute("Show databases")
for dtb in mycurr:
    print(dtb)
cn.close()