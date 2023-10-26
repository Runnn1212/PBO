# Kelas Induk (Super Class)
class KomputerWarnet:
    def __init__(self, nomor_pc, jenis, status):
        self.nomor_pc = nomor_pc
        self.jenis = jenis
        self.status = status

    def info(self):
        return f"Nomor PC: {self.nomor_pc}, Jenis: {self.jenis}, Status: {self.status}"

    def pesan(self):
        if self.status == "Tersedia":
            self.status = "Terpesan"
            return f"Anda telah memesan PC nomor {self.nomor_pc}. Silakan gunakan sekarang."
        else:
            return f"PC nomor {self.nomor_pc} sedang dipakai."

    def selesai(self):
        if self.status == "Terpesan":
            self.status = "Tersedia"
            return f"Terima kasih telah menggunakan PC nomor {self.nomor_pc}."
        else:
            return f"PC nomor {self.nomor_pc} belum dipesan."

# Kelas Anak (Sub Class)
class KomputerGaming(KomputerWarnet):
    def __init__(self, nomor_pc):
        super().__init__(nomor_pc, "Gaming PC", "Tersedia")

    def info(self):
        return f"Nomor PC: {self.nomor_pc}, Jenis: Gaming PC, Status: {self.status}"

# Main Program
if __name__ == "__main__":
    try:
        # Membuat objek KomputerWarnet
        pc1 = KomputerGaming(1)
        pc2 = KomputerGaming(2)

        # Memanggil metode info dan pesan dari KomputerGaming
        print("Info Komputer Warnet:")
        print(pc1.info())
        print(pc2.info())
        print(pc1.pesan())
        print(pc1.pesan())
        print(pc2.pesan())
        print(pc1.selesai())
        print(pc2.selesai())

    except Exception as e:
        print("Terjadi kesalahan:", str(e))
