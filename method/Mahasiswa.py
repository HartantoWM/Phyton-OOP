# membuat class dengan kata kunci "class"

class mahasiswa:
    # atribut 
    def __init__(self, nim, nama, rombel):
    # variabel objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
        
    # method 
    def lulus(self, nilai):
        if(nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
        # class mahasiswa memiliki 3 atribut dan 1 fungsi
    
    def cetak(self):
        print("nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)
            
        
# membuat objek 
mahasiswa1 = mahasiswa("0101010110", "tnto", "TI-05")


mahasiswa1.cetak()

mahasiswa2 = mahasiswa("020202020", "SIUU", "TI-05")


mahasiswa2.cetak()
