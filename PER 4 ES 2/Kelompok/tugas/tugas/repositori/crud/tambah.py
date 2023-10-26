from repositori.database.tugas_akhir import tugas_akhir

def tambahkan_form():
    judul = input("Masukkan judul tugas akhir : ")
    nim = input("Masukkan NIM mahasiswa : ")
    tahun = input("Masukkan tahun tugas akhir : ")
    dosen = input("Masukkan dosen pembimbing : ")
    
    tugas = (judul, nim, tahun, dosen)
    
    if any(existing_tugas == tugas for existing_tugas in tugas_akhir):
        print("Tugas akhir dengan NIM dan judul yang sama sudah ada.")
        
    else:
        tugas_akhir.append(tugas)
        print("Form tugas akhir berhasil ditambahkan.")