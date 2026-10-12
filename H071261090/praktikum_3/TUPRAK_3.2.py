print("=== Setup Denah Bioskop NontonYuk ===")

while True:
    try:
        n = int(input("Masukkan jumlah baris: "))

        if n <= 0:
            print("Jumlah baris harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input baris harus berupa angka!")

while True:
    try:
        m = int(input("Masukkan jumlah kursi per baris: "))
        if m <= 0:
            print("Jumlah kursi harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("\n=== Daftar Kursi Tersedia ===")

for baris in range(1, n + 1):
    for kursi in range(1, m + 1):

        if kursi == 13:
            continue

        if baris == 1:
            if kursi % 2 == 1:
                print("Baris", baris, "- Kursi", kursi)
        else:
            print("Baris", baris, "- Kursi", kursi)