print("--- Sistem Reservasi PO BUS ---")

while True:
    try:
        n = int(input("Masukkan maksimal kursi bus: "))

        if n <= 0:
            print("Jumlah kursi harus berupa angka!")
            continue

        break

    except:
        print("Input jumlah kursi harus berupa angka!")


print("--- Sistem Reservasi PO BUS Dimulai ---")

kursi_terisi = 0
total_pendapatan = 0

while kursi_terisi < n:
    sisa = n - kursi_terisi
    print(f"Sisa kursi: {sisa}")

    try:
        jumlah = int(input("Masukkan umur penumpang: "))

        if jumlah < 0:
            print("Umur tidak valid!")
            continue

    except:
        print("Input umur harus berupa angka!")
        continue

    if jumlah <= 5:
        kategori = "Balita"
        harga = 0
    elif jumlah <= 12:
        kategori = "Anak"
        harga = 50000
    else:
        kategori = "Dewasa"
        harga = 100000

    print(f"Kategori: {kategori} - Harga: Rp {harga}")

    kursi_terisi += 1
    total_pendapatan += harga


print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")