from repositori.crud.lihat import lihat_form
from repositori.crud.upload import upload_tugas_akhir

def menu_mahasiswa():
    while True:
        print("\nMenu Mahasiswa")
        print("1. Lihat Form Tugas Akhir")
        print("2. Upload Tugas Akhir")
        print("3. Keluar")

        choice = input("Pilih menu : ")

        if choice == "1":
            lihat_form()
        elif choice == "2":
            upload_tugas_akhir()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")