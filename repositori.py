# List tugas akhir
tugas_akhir = []

# Fungsi login
def login():
    while True:
        print("\tHalaman Login\t")
        print("--------------------------------")
        usernameInput = input("Masukkan username anda : ")
        passwordInput = input("Masukkan password anda : ")
        print("-------DATA DIKONFIRMASI--------")

        if usernameInput == "admin" and passwordInput == "admin":
            print("\n----------------------------------------")
            print("Login diterima, selamat datang Admin")
            print("----------------------------------------")
            menu_admin()
        elif usernameInput == "mahasiswa" and passwordInput == "mahasiswa":
            print("\n----------------------------------------")
            print("Login diterima, selamat datang Mahasiswa")
            print("----------------------------------------")
            menu_mahasiswa()
        else:
            print("\n----------------------------------------")
            print("Login ditolak, silahkan coba lagi..")
            print("----------------------------------------")

# Fungsi menu admin
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

# Fungsi tambahkan form
def tambahkan_form():
    judul = input("Masukkan judul tugas akhir : ")
    if judul in tugas_akhir:
        print("Judul tugas akhir sudah ada dalam daftar.")
    else:
        tugas_akhir.append(judul)
        print("Form tugas akhir berhasil ditambahkan.")

# Fungsi lihat form
def lihat_form():
    if tugas_akhir:
        print("\nDaftar Form Tugas Akhir :")
        for form in tugas_akhir:
            print(form)
    else:
        print("\nBelum ada tugas akhir yang ditambahkan oleh admin.")

# Fungsi menu mahasiswa
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

# Fungsi upload tugas akhir
def upload_tugas_akhir():
    if not tugas_akhir:
        print("Admin belum menambahkan tugas akhir atau tugas akhir telah diselesaikan.")
        return
    judul_tugas = input("Masukkan judul tugas akhir yang selesai : ")
    if judul_tugas in tugas_akhir:
        tugas_akhir.remove(judul_tugas)
        print("Tugas akhir berhasil ditandai sebagai selesai.")
    else:
        print("Judul tugas akhir tidak valid atau belum ditambahkan oleh admin.")

print("\n=================================")
print(" Selamat Datang di Repositori ")
print("=================================")
print()
print("*******\tSilahkan Login\t*******")
print("untuk melanjutkan ke repositori\n")
login()