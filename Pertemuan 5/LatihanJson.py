import json

x = {
    "nama" : "Chan",
    "Usia" : 30,
    "Menikah" : True,
    "Cerai" : False,
    "children" : ("Umar", "Rasyid"),
    "pets" : None,
    "Mobil" : [
        {"model": "Toyota Avanza", "mpg": 27.5},
        {"model": "Mitsubishi Mirage", "mpg": 21.4}
    ]
}

#cetak data json
print("Nama Karyawan: ", x["nama"])
print("-------cetak parser data json")
#use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))