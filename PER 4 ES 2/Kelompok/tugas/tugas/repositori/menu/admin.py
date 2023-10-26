from repositori.crud.tambah import tambahkan_form
from repositori.crud.lihat import lihat_form

def menu_admin():
    while True:
        print("\nMenu Admin")
        print("1. Tambahkan Form Tugas Akhir")
        print("2. Lihat Form Tugas Akhir")
        print("3. Keluar")

        choice = input("Pilih menu : ")

        if choice == "1":
            tambahkan_form()
        elif choice == "2":
            lihat_form()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")