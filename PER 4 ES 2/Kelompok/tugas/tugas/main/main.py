from sys import path
path.append('D:\\Kuliah\\Semester 3\\Pemrogaman Ber Orientasi Objek\\Kelompok 5\\tugas\\tugas')

from repositori.menu.admin import menu_admin
from repositori.menu.mahasiswa import menu_mahasiswa

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

print("\n=================================")
print(" Selamat Datang di Repositori ")
print("=================================")
print()
print("*****\tSilahkan Login\t*****")
print("untuk melanjutkan ke repositori\n")
login()
            
