from modul.rental import KomputerGaming
if __name__ == "__main":
    try:
        # Membuat objek KomputerWarnet
        pc1 = KomputerGaming(1)
        pc2 = KomputerGaming(2)

        # Memanggil metode info dan pesan dari KomputerGaming
        print("Info Komputer Warnet:")
        print(pc1.info())
        print(pc2.info())

        # Pesan dan gunakan komputer
        print(pc1.pesan())
        print(pc1.pesan())
        print(pc2.pesan())

        # Kembalikan komputer yang sudah digunakan
        print(pc1.selesai())
        print(pc2.selesai())

    except Exception as e:
        print("Terjadi kesalahan:", str(e))
