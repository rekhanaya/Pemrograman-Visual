#Nama           : Rekha Inaya Putri
#NIM            : 2022071044
#Hari/Tanggal   : Jumat, 1 Maret 2024

import math

class BangunDatar:
    def luasSegitiga(self, alas, tinggi):
        return alas * tinggi * 0.5
    
    def luasPersegi(self, sisi):
        return sisi*sisi
    
    def kelilingPersegi(self,sisi):
        return 4*sisi
    
    def luasPesegiPanjang(self, panjang, lebar):
        return panjang*lebar
    
    def kelilingPersegiPanjang(self, panjang, lebar):
        return 2*panjang*lebar
    
    def luasLingkaran(self, diameter):
        jari_jari = diameter/2
        return math.pi*(jari_jari**2)
    
    def kelilingLingkaran(self, jari_jari):
        return math.pi*jari_jari*2
    