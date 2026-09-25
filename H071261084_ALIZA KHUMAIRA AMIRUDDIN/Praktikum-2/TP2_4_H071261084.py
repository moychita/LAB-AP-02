tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota):  ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam):  ").capitalize()
tipe_pengunjung = input("Masukkan tipe pengunjung (Dewasa/Anak):  ").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            rekomendasi = "Paket A"
        else:
            if waktu == "Malam" and tipe_pengunjung == "Dewasa":
                rekomendasi = "Paket C"
            else:
                rekomendasi = "Tidak ada paket yang cocok"
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket B"
        else:
            if waktu == "Malam" and tipe_pengunjung == "Dewasa":
                rekomendasi = "Paket C"
            else:
                rekomendasi = "Tidak ada paket yang cocok"
    case "Kota":
        if waktu == "Malam":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"
    case _:
        rekomendasi = "Tidak sesuai"

print("Paket Rekomendasi:  ", rekomendasi)