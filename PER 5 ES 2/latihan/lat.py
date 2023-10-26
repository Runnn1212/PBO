#pembuatan class
class Mahasiswa:
    #konstruktor
    def __init__(self):
        self.nim = ""
        self.nama = ""
    #method set_data
    def set_data(self, nim, nama):
        self.nim = nim
        self.nama = nama
    #method tampil_data
    def tampil_data(self):
        print("NIM:", self.nim)
        print("Nama:", self.nama)
        
#pemanggilan fungsi class
mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()
mahasiswa3 = Mahasiswa()

#memasukkan data dengan set_data
mahasiswa1.set_data("2231730146", "Mohamad Saiful Yusuf\n")
mahasiswa2.set_data("2231730111", "rr heidy yulia\n")
mahasiswa3.set_data("2231730016", "firman koirul anam\n")

#menampilkan data dengan tampil_data
mahasiswa1.tampil_data()
mahasiswa2.tampil_data()
mahasiswa3.tampil_data()

#Membuat Anak Kelas
class Aktivis(Mahasiswa):
    #kontruktor anak kelas
    def __init__(self):
        super().__init__()
        self.organisasi = ""
    #method anak kelas
    def set_org(self, organisasi):
        self.organisasi = organisasi

    def tampil_org(self):
        print("Organisasi:", self.organisasi)

# Pemanggilan Method Dari class aktivis dan juga turunan dari class mahasiswa
aktivis1 = Aktivis()
aktivis2 = Aktivis()
aktivis3 = Aktivis()
aktivis1.set_data("2231730146", "Mohamad Saiful Yusuf")
aktivis2.set_data("2231730111", "rr heidy yulia")
aktivis3.set_data("2231730016", "firman koirul anam")
aktivis1.set_org("BEM\n")
aktivis2.set_org("HIMA\n")
aktivis3.set_org("UKM\n")
aktivis1.tampil_data()
aktivis1.tampil_org()
aktivis2.tampil_data()
aktivis2.tampil_org()
aktivis3.tampil_data()
aktivis3.tampil_org()

