# Dalam file rumus/volbal.py

def volume():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    hasil_volume = panjang * lebar * tinggi
    print(f"Volume balok dengan panjang {panjang}, lebar {lebar}, dan tinggi {tinggi} adalah {hasil_volume}")
    return hasil_volume


