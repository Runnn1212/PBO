class Pembayaran:
    def __init__(self, tiket):
        self.tiket = tiket
        self.hitung_harga()

    def hitung_harga(self):
        self.total_harga = self.tiket.jumlah_tiket * self.tiket.harga_per_tiket

    def bayar(self):
        print(f"Total harga: Rp.{self.total_harga}  \nSilahkan bayar.")
        print(f"~~~Terima Kasih Sudah Mengunjungi Aplikasi Kami~~~")