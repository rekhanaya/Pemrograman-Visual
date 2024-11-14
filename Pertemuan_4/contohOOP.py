class Mobil:
    def __init__(self):
        self.merek = "Avanza"
        self.warna = "Hitam"
        self.noPol = "B 1234 ABC"
        self.pemilik ="Chan" 

    def getMobil(self):
        return "Merek: " + self.merek + "\nWarna: " +self.warna + "\nNomor Polisi: " + self.noPol + "\nPemilik: " +self.pemilik

    def setWarnaMobil(self, warna):
        self.warna = warna

m = Mobil()
print(m.getMobil())
m.setWarnaMobil("Merah")
print(m.getMobil())