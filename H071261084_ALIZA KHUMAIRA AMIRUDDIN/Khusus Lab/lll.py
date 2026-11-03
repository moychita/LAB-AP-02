import re
teks = "Beli 3 buku, 2 Pensil, dan 10 map"
# angka = re.findall('\d+', teks)
angka = [int(x) for x in re.findall('\d+', teks)]

print("Angka ditemukan:", angka)
print("Jumlah angka:", len(angka))
print("Total:", sum(angka))