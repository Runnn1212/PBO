from repositori.database.tugas_akhir import tugas_akhir

def upload_tugas_akhir():
    if not tugas_akhir:
        print("Admin belum menambahkan tugas akhir atau tugas akhir telah diselesaikan.")
        return

    nim = input("Masukkan NIM mahasiswa yang menyelesaikan tugas akhir : ")
    judul_tugas = input("Masukkan judul tugas akhir yang selesai : ")

    found = False
    for tugas in tugas_akhir:
        judul, nim_tugas, _, _ = tugas
        if judul == judul_tugas and nim_tugas == nim:
            tugas_akhir.remove(tugas)
            print("Tugas akhir berhasil ditandai sebagai selesai.")
            found = True
            break
    if not found:
        print("Tidak dapat menemukan tugas akhir dengan judul tersebut atau NIM yang sesuai.")






