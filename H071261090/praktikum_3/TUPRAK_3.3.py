while True:
    try:
        kursi = int(input("Masukkan maksimal kursi bus: "))

        if kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue

        break

    except ValueError:
        print("Input jumlah kursi harus berupa angka!")


sisa_kursi = kursi
total = 0

print("\n=== Sistem Reservasi PO BUS Dimulai ===")

while sisa_kursi > 0:
    print("\nSisa kursi:", sisa_kursi)

    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0:
            print("Umur tidak valid!")
            continue

        elif umur <= 5:
            harga = 0
            kategori = "Balita - Tiket Gratis (Rp 0)"

        elif umur <= 12:
            harga = 50000
            kategori = "Anak - Harga: Rp 50.000"

        else:
            harga = 100000
            kategori = "Dewasa - Harga: Rp 100.000"

        print("Kategori:", kategori)

        total = total + harga
        sisa_kursi = sisa_kursi - 1

    except ValueError:
        print("Input harus berupa angka!")


print("\n=== Semua Kursi Terisi ===")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total)