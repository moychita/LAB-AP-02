import re

data_sebelum = []
data_setelah = []
nomor_valid = []

print("=== Pembersihan Data Nomor Telepon ===")

jumlah = int(input("\nMasukkan jumlah data: "))
print()

for i in range(jumlah):
    nomor = input(f"Nomor ke-{i+1}: ")
    data_sebelum.append(nomor)
    nomor_bersih = re.sub(r'[\s-]', '', nomor)
    data_setelah.append(nomor_bersih)
    if re.fullmatch(r'\d{10,13}', nomor_bersih):
        nomor_valid.append(nomor_bersih)

print()
print("--- Hasil Pembersihan ---")

for i in range(jumlah):
    print()
    print(f"Data {i+1}:")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_setelah[i])
    if re.fullmatch(r'\d{10,13}', data_setelah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")

print()
print("Jumlah nomor valid:", len(nomor_valid))