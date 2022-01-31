class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


Tayfun = Insan("Tayfun", "Dereli", "24", "Türkiye", "İstanbul")
Tayfun.yetenek_ekle("bisiklete binme")
Tayfun.yetenek_ekle("python")
print(Tayfun.kisi_bilgileri())

