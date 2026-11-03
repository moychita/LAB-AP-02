import re

def bersihkan_nomor(nomor):
    return re.sub(r"[ -]", "", nomor)

def validasi_nomor(nomor):
    pattern = r"^[0-9]{10,13}$"
    return re.match(pattern, nomor) 

print("=== Pembersihan Data Nomor Telepon ===")
jumlah = int(input("Masukkan jumlah data: "))

data_sebelum = []
data_sesudah = []
nomor_valid = []
status_data = []

for i in range(jumlah):
    nomor = input(f"Nomor ke-{i+1}: ")

    data_sebelum.append(nomor)

    hasil = bersihkan_nomor(nomor)
    data_sesudah.append(hasil)

    if validasi_nomor(hasil):
        status = "Valid"
        nomor_valid.append(hasil)
    else:
        status = "Tidak valid"

    status_data.append(status)

print("=== Hasil Pembersihan ===")

for i in range(jumlah):
    print(f"Data {i+1}:")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])
    print("Status  :", status_data[i])

print(f"Jumlah nomor valid: {len(nomor_valid)}")