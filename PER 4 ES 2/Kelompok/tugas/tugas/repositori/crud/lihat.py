from repositori.database.tugas_akhir import tugas_akhir

def lihat_form():
    nim_cari = input("Masukkan NIM mahasiswa untuk mencari tugas akhir: ")
    found = False
    
    if tugas_akhir:
        print("\nDaftar Form Tugas Akhir :")
        for form in tugas_akhir:
            judul, nim, tahun, dosen = form
            if nim == nim_cari:
                print(f"Judul: {judul}")
                print(f"NIM: {nim}")
                print(f"Tahun: {tahun}")
                print(f"Dosen Pembimbing: {dosen}")
                print("--------------------")
                found = True
        
        if not found:
            print("Tidak ada tugas akhir yang ditemukan untuk NIM tersebut.")
    else:
        print("\nBelum ada tugas akhir yang ditambahkan oleh admin.")