import math

def luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari**2
    return luas

def luas_persegi(sisi):
    luas = sisi**2
    return luas

def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Main program
def lingkaran():
    # Menghitung luas lingkaran
    radius = float(input("Masukkan panjang jari-jari lingkaran: "))
    hasil_lingkaran = luas_lingkaran(radius)
    print(f"Luas lingkaran dengan jari-jari {radius} adalah {hasil_lingkaran}")
def persegi():
    # Menghitung luas persegi
    sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
    hasil_persegi = luas_persegi(sisi_persegi)
    print(f"Luas persegi dengan sisi {sisi_persegi} adalah {hasil_persegi}")
def segitiga():
    alas = float(input("\nMasukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    hasil_segitiga = luas_segitiga(alas, tinggi)
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {hasil_segitiga}")
