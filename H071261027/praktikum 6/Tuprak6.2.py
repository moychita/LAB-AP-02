
def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Error! Kandidat '{pilihan}' tidak terdaftar.")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print(
            f"Suara untuk '{pilihan}' berhasil dicatat!"
        )


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("========================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    if len(perolehan) == 0:
        print("Belum ada kandidat.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = []

    for kandidat, jumlah in perolehan.items():
        if jumlah == suara_tertinggi:
            pemenang.append(kandidat)

    if len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {suara_tertinggi} suara!"
        )

    print("========================================")


# PROGRAM UTAMA

kandidat_set = set()
rekap_suara = {}

print("========================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

# FASE PENDAFTARAN KANDIDAT
print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    ).strip()

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

while len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat!")
    nama = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    ).strip()

    if nama != "":
        daftar_kandidat(kandidat_set, nama)
    else:
        print("Pendaftaran harus dilanjutkan.")

print("\nKandidat terdaftar:", kandidat_set)

# FASE PEMUNGUTAN SUARA
print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input(
        "\nNama pemilih (kosongkan untuk selesai): "
    ).strip()

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara,
        kandidat_set,
        nama_pemilih,
        pilihan
    )

# MENGHITUNG DAN MENAMPILKAN HASIL
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
