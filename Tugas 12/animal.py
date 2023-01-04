class animal:
    nama = ""
    makanan = ""
    habitat = ""
    berkembang = ""

    def __init__(self, nama, makanan, habitat, berkembang):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang = berkembang

    def cetak(self):
        print("\n==================",
            "\nNama \t\t :", self.nama,
            "\nJenis Makanan \t\t :", self.makanan,
            "\nHabitat \t\t :", self.habitat,
            "\nBerkembang Biak \t\t :", self.berkembang,           
            )

