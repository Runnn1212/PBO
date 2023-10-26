from Modul.Tiket import TiketHaji
from Modul.Tiket import TiketUmroh
from Modul.Bayar import Pembayaran

def main():
    try:
        print("***_Selamat Datang Di Aplikasi Travel Kami_***\n")
        kelas = input("Silahkan Pilih kelas tiket (Haji/Umroh): ")

        # Validasi input kelas tiket
        while kelas not in ["Haji", "Umroh"]:
            print("Kelas tiket tidak tersedia. Silakan pilih kembali.")
            kelas = input("Silahkan Pilih kelas tiket (Haji/Umroh): ")

        jumlah_tiket = int(input("Jumlah tiket yang ingin dipesan: "))

        # Validasi jumlah tiket (tidak boleh <= 0)
        while jumlah_tiket <= 0:
            print("Jumlah tiket harus lebih dari 0. Silakan masukkan kembali.")
            jumlah_tiket = int(input("Jumlah tiket yang ingin dipesan: "))

        if kelas == "Haji":
            tiket = TiketHaji(jumlah_tiket)
        elif kelas == "Umroh":
            tiket = TiketUmroh(jumlah_tiket)

        print("\nPesanan Anda Berhasil Dengan Rincian Sebagai Berikut :")
        print(tiket.tampilan())  # Override

        pembayaran = Pembayaran(tiket)
        pembayaran.bayar()

    except Exception as e: # Exception(Output) Yg akan keluar apabila Try(Input)/Program Error
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    main()
