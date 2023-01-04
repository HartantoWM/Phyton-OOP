from animal import *

class burung(animal):
    sifat = ""
    jenis = ""

    def __init__(self, nama, makanan, habitat, berkembang, jenis, sifat):
        super().__init__(nama, makanan, habitat, berkembang,)
        self.sifat = sifat
        self.jenis = jenis

    def cetak(self):
        super().cetak()
        print("sifat hewan \t :", self.sifat,
            "\nJenis \t\t :",self.jenis,
            "\n===================================")