from sys import path
path.append('D:\\Kuliah\\Semester 3\\Pemrogaman Ber Orientasi Objek\\latihan')

from rumus.luas.pl import lingkaran,persegi,segitiga
print(lingkaran())
print(segitiga())
print(persegi())

import rumus.volume.tabung.voltab
print(rumus.volume.tabung.voltab.volume())

import rumus.volume.balok.volbal
print(rumus.volume.balok.volbal.volume())