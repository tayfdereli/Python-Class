class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi


class Soru(Ogrenci):
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        super().__init__(ogrenciAdi, ogrenciSoyadi, ogrenciSinifi)

    def netSayisi(self):
        dogruSoruSayisi = float(input("Doğru soru sayısı = "))
        yanlisSoruSayisi = float(input("Yanlış soru sayısı = "))
        if dogruSoruSayisi + yanlisSoruSayisi != 50:
            print("Soru sayısı toplamı 50 olmalı")
            return self.netSayisi()
        netHesabi = dogruSoruSayisi - (yanlisSoruSayisi * 0.25)
        return netHesabi

    def Hesapla(self):
        netSayisi = self.netSayisi()
        puan = netSayisi * 2
        print("{}. sınıf öğrencisi {} {}'nin neti = {}, puanı ise = {}".format(self.ogrenciSinifi, self.ogrenciAdi,
                                                                               self.ogrenciSoyadi, netSayisi,
                                                                               puan))


Tayfun = Ogrenci("Tayfun", "Dereli", "12")
Soru(Tayfun.ogrenciAdi, Tayfun.ogrenciSoyadi, Tayfun.ogrenciSinifi).Hesapla()
